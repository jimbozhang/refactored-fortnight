from datetime import datetime, timedelta
from pathlib import Path
from typing import Tuple

import pandas as pd

from fetch_data_to_files import fetch_stock_ids
from paths import STOCK_IDS_CSV, VOL_CSVS_DIR


def yesterday_exlude_weekend(today: datetime) -> datetime:
    while True:
        yesterday = today - timedelta(days=1)
        if yesterday.weekday() < 5:
            return yesterday


def cal_volume_factor(info: pd.DataFrame, time: str = None) -> Tuple[float, float, float]:
    '''
    Calculate the rate: (the highest volume of today) / (the highest volume of yesterday)

    Args:
        info (pd.DataFrame): from ak.stock_zh_a_hist_min_em

    Returns:
        Tuples[float, float, float]:
            the highest volume of today
            the highest volume of yesterday
            rate of the above
    '''
    today = time if time is not None else datetime.now().isoformat(" ", "seconds")
    today = datetime.fromisoformat(today)
    yesterday = yesterday_exlude_weekend(today)

    max_vol_today = 0
    max_vol_yesterday = 0
    for time, volume in info[['时间', '成交量']].values:
        time = datetime.fromisoformat(time)
        if time.date() == yesterday.date():
            if volume > max_vol_yesterday:
                max_vol_yesterday = volume
        if time.date() == today.date():
            if volume > max_vol_today:
                max_vol_today = volume

    rate = max_vol_today / max_vol_yesterday
    return max_vol_today, max_vol_yesterday, rate


def search(ids: pd.Series, csv_dir: Path, time: str = None) -> pd.DataFrame:
    pd.DataFrame
    for id in ids:
        csv_path = csv_dir / f'{id}.csv'
        max_vol_today, max_vol_yesterday, rate = cal_volume_factor(pd.read_csv(csv_path), time)
        pass


if __name__ == '__main__':
    ids = fetch_stock_ids(STOCK_IDS_CSV)
    search(ids, VOL_CSVS_DIR, time='2022-09-02 09:42:05')
