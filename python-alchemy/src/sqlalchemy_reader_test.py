import unittest
from sqlalchemy_reader import SqlAlchemyReader
from model.skill import Skill


class SqlAlchemyReaderTest(unittest.TestCase):
    def test_skill_all(self):
        skill = SqlAlchemyReader.get_skill_by_id('00001')
        print(skill)

        for skill in SqlAlchemyReader.get_skill_all():
            print(skill)

        for skill in SqlAlchemyReader.get_skill_all_order_by_name():
            print(skill)

        for skill in SqlAlchemyReader.get_skill_by_name(name='AWS'):
            print(skill)

        for skill in SqlAlchemyReader.get_skill_by_names(['java1.8', 'AWS']):
            print(skill)

    def test_engineer_all(self):
        engineer = SqlAlchemyReader.get_engineer_with_skill_by_id('00001')
        print(engineer)
        for engineer_skill in engineer.engineer_skill:
            print(engineer_skill.skill.name)

        for engineer in SqlAlchemyReader.get_engineer_with_skill_all():
            print(engineer)

        for engineer in SqlAlchemyReader.get_engineer_with_skill_by_skill_name('python2'):
            print(engineer)

        for engineer in SqlAlchemyReader.get_engineer_with_skill_all_outer_join():
            print(engineer)


if __name__ == "__main__":
    unittest.main()