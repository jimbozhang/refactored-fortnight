import akshare as ak

CSV_FILES = {
    'stock_ids': 'stocks.csv',
}


def stock_ids_to_csv(filename):
    df = ak.stock_zh_a_spot()
    df.loc[:, ['代码', '名称']].to_csv(filename, index=False)


if __name__ == '__main__':
    stock_ids_to_csv(CSV_FILES['stock_ids'])
