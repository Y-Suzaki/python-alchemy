from sqlalchemy_settings import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relation
from model.skill import Skill


class EngineerSkill(Base):
    # テーブル名やカラム定義は必須
    __tablename__ = 'engineer_skill'

    # 複合Primary Keyの場合
    engineer_id = Column(String(5), ForeignKey('engineer.id'), primary_key=True)
    skill_id = Column(String(5), ForeignKey('skill.id'), primary_key=True)

    skill = relation(Skill)

    def __str__(self):
        return '[engineer_id={}, skill_id={}]'.format(self.engineer_id, self.skill_id)

