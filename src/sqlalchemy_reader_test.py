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


if __name__ == "__main__":
    unittest.main()