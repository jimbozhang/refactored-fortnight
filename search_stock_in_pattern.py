from datetime import datetime, timedelta
from pathlib import Path
from typing import Tuple

import pandas as pd

from fetch_data_to_files import fetch_stock_id_names
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

    rate = max_vol_today / max_vol_yesterday if max_vol_yesterday != 0 else 1
    return max_vol_yesterday, max_vol_today, rate


def make_report(ids: pd.DataFrame, csv_dir: Path, time: str = None) -> pd.DataFrame:
    report = pd.DataFrame(columns=['股票代码', '股票名称', '昨天最高成交', '今天最高成交', '倍数'])
    for id, name in ids.values:
        csv_path = csv_dir / f'{id}.csv'
        report.loc[len(report.index)] = [id, name] + list(cal_volume_factor(pd.read_csv(csv_path), time))

    return report.sort_values(by='倍数', ascending=False)


if __name__ == '__main__':
    ids = fetch_stock_id_names(STOCK_IDS_CSV)
    report = make_report(ids, VOL_CSVS_DIR, time='2022-09-02 09:42:05')
    report.to_csv('output.csv')
