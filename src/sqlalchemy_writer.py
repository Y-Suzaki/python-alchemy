from session_context import SessionContext
from model.skill import Skill


class SqlAlchemyWriter:
    def add_skill(self, skill):
        with SessionContext() as session:
            session.add(skill)

    def remove_skill(self, id):
        with SessionContext() as session:
            target = session.query(Skill).get(id)
            if target is not None:
                session.delete(target)

    def update_skill(self):
        pass

    def add_engineer(self):
        pass

    def remove_enginner(self):
        pass

    def update_engnieer(self):
        pass


SqlAlchemyWriter().remove_skill(id='00001')
SqlAlchemyWriter().add_skill(Skill(id='00001', name='python3'))
