from session_context import SessionContext
from model.skill import Skill
from model.engineer import Engineer
from model.engineer import EngineerSkill
from sqlalchemy.orm import eagerload
from sqlalchemy.orm import joinedload
from sqlalchemy import asc


class SqlAlchemyReader:
    @staticmethod
    def get_skill_by_id(id):
        with SessionContext() as session:
            return session.query(Skill).get(id)

    @staticmethod
    def get_skill_all(limit=10):
        with SessionContext() as session:
            return session.query(Skill)\
                .limit(limit).all()

    @staticmethod
    def get_skill_all_order_by_name(limit=10):
        with SessionContext() as session:
            return session.query(Skill)\
                .order_by(asc(Skill.name))\
                .limit(limit).all()

    @staticmethod
    def get_skill_by_name(name):
        with SessionContext() as session:
            return session.query(Skill)\
                .filter(Skill.name == name).all()

    @staticmethod
    def get_skill_by_names(names):
        with SessionContext() as session:
            return session.query(Skill)\
                .filter(Skill.name.in_(names)).all()

    @staticmethod
    def get_engineer_by_id(id):
        with SessionContext() as session:
            return session.query(Skill).get(id)

    @staticmethod
    def get_engineer_with_skill_by_id(engineer_id):
        with SessionContext() as session:
            return session.query(Engineer) \
                .options(joinedload(Engineer.engineer_skill).joinedload(EngineerSkill.skill))\
                .get(engineer_id)

    @staticmethod
    def get_engineer_with_skill_all():
        with SessionContext() as session:
            return session.query(Engineer)\
                .join(EngineerSkill)\
                .join(Skill) \
                .options(joinedload(Engineer.engineer_skill).joinedload(EngineerSkill.skill)).all()

    @staticmethod
    def get_engineer_with_skill_by_skill_name(skill_name):
        with SessionContext() as session:
            return session.query(Engineer)\
                .join(EngineerSkill)\
                .join(Skill)\
                .filter(Skill.name == skill_name)\
                .options(joinedload(Engineer.engineer_skill).joinedload(EngineerSkill.skill)).all()

    @staticmethod
    def get_engineer_with_skill_all_outer_join():
        with SessionContext() as session:
            return session.query(Engineer)\
                .outerjoin(EngineerSkill) \
                .outerjoin(Skill) \
                .options(joinedload(Engineer.engineer_skill).joinedload(EngineerSkill.skill)).all()
