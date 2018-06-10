from session_context import SessionContext
from model.skill import Skill


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

    def add_engineer(self):
        pass

    def remove_enginner(self):
        pass

    def update_engnieer(self):
        pass
