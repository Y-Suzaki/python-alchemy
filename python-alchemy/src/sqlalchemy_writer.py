from session_context import SessionContext
from model.skill import Skill
from model.engineer import Engineer
from model.engineer_skill import EngineerSkill


class SqlAlchemyWriter:
    @staticmethod
    def add_skill(skill):
        with SessionContext() as session:
            session.add(skill)
        return skill

    @staticmethod
    def remove_skill(id):
        with SessionContext() as session:
            target = session.query(Skill).get(id)
            if target is not None:
                session.delete(target)

    @staticmethod
    def update_skill(id, name):
        with SessionContext() as session:
            target = session.query(Skill).get(id)
            target.name = name

    @staticmethod
    def add_engineer(engineer):
        with SessionContext() as session:
            session.add(engineer)
        return engineer

    @staticmethod
    def remove_engineer(id):
        with SessionContext() as session:
            target = session.query(Engineer).get(id)
            if target is not None:
                session.delete(target)

    @staticmethod
    def update_engineer(id, name, age):
        with SessionContext() as session:
            target = session.query(Engineer).get(id)
            target.name = name
            target.age = age

    @staticmethod
    def add_engineer_skill(engineer_skill):
        with SessionContext() as session:
            session.add(engineer_skill)
        return engineer_skill

    @staticmethod
    def remove_engineer_skill(engineer_id, skill_id):
        with SessionContext() as session:
            target = session.query(EngineerSkill) \
                .filter(EngineerSkill.engineer_id == engineer_id).filter(EngineerSkill.skill_id == skill_id).first()
            if target is not None:
                session.delete(target)
