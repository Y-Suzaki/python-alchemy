from sqlalchemy_settings import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relation
from model.engineer_skill import EngineerSkill


class Engineer(Base):
    # テーブル名やカラム定義は必須
    __tablename__ = 'engineer'
    id = Column(String(5), primary_key=True)
    name = Column(String(100))
    age = Column(Integer)

    engineer_skill = relation(EngineerSkill)

    def __str__(self):
        return '[id={}, name={}, age={}]'.format(self.id, self.name, self.age)

print(Engineer())




