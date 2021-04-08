from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric, Date
import constants

class MySQLServer:
    def __init__(self):
        self.engine = create_engine(f'mysql+mysqlconnector://{constants.USER}:{constants.PASSWORD}@{constants.HOST}/{constants.DATABASE}', echo=True)
        self.meta = MetaData()
        self.stocks = Table(
            'stocks', self.meta,
            Column('id', Integer, primary_key = True),
            Column('date', Date, nullable=True),
            Column('close', Numeric),
            Column('volume', Numeric),
            Column('label', Numeric),
            Column('change', Numeric),
            Column('change_percent', Numeric)
        )

    def get_engine(self):
        return self.engine

    def get_table(self):
        return self.stocks
    
    def get_meta(self):
        return self.meta

    def create_table(self, meta, engine):
        meta.create_all(engine)

    def start_connection(self, engine):
        return engine.connect()
