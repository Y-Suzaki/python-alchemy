from session_context import SessionContext
from model.skill import Skill
from model.engineer import Engineer
from model.engineer import EngineerSkill
from sqlalchemy.orm import eagerload


class SqlAlchemyReader:
    @staticmethod
    def get_skill_by_id(id):
        with SessionContext() as session:
            return session.query(Skill).get(id)

    @staticmethod
    def get_skill_all(limit=10):
        with SessionContext() as session:
            return session.query(Skill).limit(limit).all()

    @staticmethod
    def get_skill_by_name(name):
        with SessionContext() as session:
            return session.query(Skill).filter(Skill.name == name).all()

    @staticmethod
    def get_engineer_by_id(id):
        with SessionContext() as session:
            return session.query(Skill).get(id)

    @staticmethod
    def get_engineer_with_skill(engineer_id):
        with SessionContext() as session:
            return session.query(Engineer).options(eagerload('engineer_skill'), eagerload('engineer_skill.skill'))\
                .get(engineer_id)
