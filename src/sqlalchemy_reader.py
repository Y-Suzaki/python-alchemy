from session_context import SessionContext
from model.skill import Skill


class SqlAlchemyReader:
    def selectById(self, id):
        with SessionContext() as session:
            return session.query(Skill).get(id)

    def selectAll(self, limit=10):
        with SessionContext() as session:
            return session.query(Skill).limit(limit).all()

    def selectByName(self, name):
        with SessionContext() as session:
            return session.query(Skill).filter(Skill.name == name).all()


skill = SqlAlchemyReader().selectById('00001')
print(skill)

skills = SqlAlchemyReader().selectAll()
for skill in skills:
    print(skill)

skills = SqlAlchemyReader().selectByName(name='AWS')
for skill in skills:
    print(skill)
