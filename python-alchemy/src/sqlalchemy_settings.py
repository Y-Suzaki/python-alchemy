from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# 環境に合わせて変更すること
DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    "root",
    "root",
    "localhost",
    "sample",
)

# echo=True 実行時にSQLが出力される
ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

# 各モデルで継承する
Base = declarative_base()
