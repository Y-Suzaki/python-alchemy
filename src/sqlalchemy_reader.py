from session_context import SessionContext
from model.skill import Skill


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
