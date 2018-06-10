import unittest
from sqlalchemy_reader import SqlAlchemyReader
from model.skill import Skill


class SqlAlchemyReaderTest(unittest.TestCase):
    def test_skill_all(self):
        skill = SqlAlchemyReader.get_skill_by_id('00001')
        print(skill)

        skills = SqlAlchemyReader.get_skill_all()
        for skill in skills:
            print(skill)

        skills = SqlAlchemyReader.get_skill_by_name(name='AWS')
        for skill in skills:
            print(skill)

    def test_engineer_all(self):
        engineer = SqlAlchemyReader.get_engineer_with_skill('00001')
        print(engineer)
        for engineer_skill in engineer.engineer_skill:
            print(engineer_skill.skill.name)


if __name__ == "__main__":
    unittest.main()