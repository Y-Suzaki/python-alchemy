import sys
sys.path.append('../')

from sqlalchemy_settings import Base
from sqlalchemy import Column, Integer, String


class Skill(Base):
    # テーブル名やカラム定義は必須
    __tablename__ = 'skill'
    id = Column(String(5), primary_key=True)
    name = Column(String(100))


