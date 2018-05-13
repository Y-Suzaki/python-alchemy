from session_context import SessionContext
from model.skill import Skill


class SqlAlchemyWriter:
    def add_skill(self, skill):
        with SessionContext() as session:
            session.add(skill)

    def remove_skill(self, id):
        pass

    def update_skill(self):
        pass

    def add_engineer(self):
        pass

    def remove_enginner(self):
        pass

    def update_engnieer(self):
        pass


SqlAlchemyWriter().add_skill(Skill(id='00001', name='python3'))
