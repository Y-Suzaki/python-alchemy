from sqlalchemy_settings import Base
from sqlalchemy import Column, Integer, String


class EngineerSkill(Base):
    # テーブル名やカラム定義は必須
    __tablename__ = 'engineer_skill'

    # 複合Primary Keyの場合
    engineer_id = Column(String(5), primary_key=True)
    skill_id = Column(String(5), primary_key=True)

    def __str__(self):
        return '[engineer_id={}, skill_id={}]'.format(self.engineer_id, self.skill_id)

