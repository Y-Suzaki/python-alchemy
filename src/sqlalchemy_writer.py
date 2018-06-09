from session_context import SessionContext
from model.skill import Skill


class SqlAlchemyWriter:
    def add_skill(self, skill):
        with SessionContext() as session:
            session.add(skill)
        return skill

    def remove_skill(self, id):
        with SessionContext() as session:
            target = session.query(Skill).get(id)
            if target is not None:
                session.delete(target)

    def update_skill(self, id, name):
        with SessionContext() as session:
            target = session.query(Skill).get(id)
            target.name = name

    def add_engineer(self):
        pass

    def remove_enginner(self):
        pass

    def update_engnieer(self):
        pass


# Skill Test
SqlAlchemyWriter().remove_skill(id='00001')
SqlAlchemyWriter().remove_skill(id='00002')
SqlAlchemyWriter().remove_skill(id='00003')

skill = SqlAlchemyWriter().add_skill(Skill(id='00001', name='python3'))
skill = SqlAlchemyWriter().add_skill(Skill(id='00002', name='java'))
skill = SqlAlchemyWriter().add_skill(Skill(id='00003', name='AWS'))

SqlAlchemyWriter().update_skill(id='00001', name='python2')
SqlAlchemyWriter().update_skill(id='00002', name='java1.8')


# Engineer Test
