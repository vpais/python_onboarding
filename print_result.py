from latest_updates import get_latest_updates
from connector_alc import MySQLServer

def print_result():

    ticker = 'FB'
    df = get_latest_updates(ticker)

    s = MySQLServer()
    eng = s.get_engine()
    stocks = s.get_table()

    cn = s.start_connection(eng)

    #print('Latest updates of {}\n------------'.format(ticker))
    for i in range(len(df)):
        # print('DATE: {} |'.format(df[i]['date']),
        # 'CLOSE: {} |'.format(df[i]['close']),
        # 'VOLUME: {} |'.format(df[i]['volume']),
        # 'LABEL: {} |'.format(df[i]['label']),
        # 'CHANGE: {} |'.format(df[i]['change']),
        # 'CHANGE PERCENT: {}'.format(df[i]['changePercent']))


        inst = stocks.insert().values(
            date = df[i]['date'],
            close = df[i]['close'],
            volume = df[i]['volume'],
            label = df[i]['label'], 
            change = df[i]['change'],
            change_percent = df[i]['changePercent'],
        )

        cn.execute(inst)

print_result()