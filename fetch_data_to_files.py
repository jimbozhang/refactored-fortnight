import os
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import akshare as ak
import pandas as pd

from paths import ROOT_DIR, STOCK_IDS_CSV, VOL_CSVS_DIR


def stock_ids_to_csv(out_csv_path: Path) -> None:
    df = ak.stock_zh_a_spot()
    df.loc[:, ['代码', '名称']].to_csv(out_csv_path, index=False)


def fetch_stock_ids(csv_path: Path, force_update_csv=False) -> pd.DataFrame:
    if force_update_csv or not Path.exists(csv_path):
        stock_ids_to_csv(csv_path)
    return pd.read_csv(csv_path).loc[:, '代码']


def fecth_and_write_stock_info(stock_id: str, out_csv_path: Path) -> str:
    info = ak.stock_zh_a_hist_min_em(symbol=stock_id, start_date="2022-09-01 09:00:00", period='1', adjust='')
    info.to_csv(out_csv_path, index=False)
    return stock_id


def update_historical_cache(stock_ids: pd.Series, out_csv_dir: Path, num_jobs: int = -1) -> None:
    Path.mkdir(out_csv_dir, exist_ok=True)
    if num_jobs < 0:
        num_jobs = os.cpu_count()

    with ThreadPoolExecutor(max_workers=num_jobs) as executor:
        for id in stock_ids:
            stock_id = re.sub(r'^[a-z]+', '', id),
            out_csv_path = out_csv_dir / f'{id}.csv'
            executor.submit(fecth_and_write_stock_info, stock_id, out_csv_path)


if __name__ == '__main__':
    Path.mkdir(ROOT_DIR, exist_ok=True)
    ids = fetch_stock_ids(STOCK_IDS_CSV)
    update_historical_cache(ids, VOL_CSVS_DIR, num_jobs=100)
