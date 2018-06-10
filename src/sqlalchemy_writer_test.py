import unittest
from sqlalchemy_writer import SqlAlchemyWriter
from model.skill import Skill
from model.engineer import Engineer


class SqlAlchemyWriterTest(unittest.TestCase):
    def test_skill_all(self):
        SqlAlchemyWriter.remove_skill(id='00001')
        SqlAlchemyWriter.remove_skill(id='00002')
        SqlAlchemyWriter.remove_skill(id='00003')

        SqlAlchemyWriter.add_skill(Skill(id='00001', name='python3'))
        SqlAlchemyWriter.add_skill(Skill(id='00002', name='java'))
        SqlAlchemyWriter.add_skill(Skill(id='00003', name='AWS'))

        SqlAlchemyWriter.update_skill(id='00001', name='python2')
        SqlAlchemyWriter.update_skill(id='00002', name='java1.8')

    def test_engineer_all(self):
        SqlAlchemyWriter.remove_engineer(id='00001')
        SqlAlchemyWriter.remove_engineer(id='00002')

        SqlAlchemyWriter.add_engineer(Engineer(id='00001', name='tanaka', age=37))
        SqlAlchemyWriter.add_engineer(Engineer(id='00002', name='hayashi', age=25))

        SqlAlchemyWriter.update_engineer(id='00001', name='tanaka', age=38)


if __name__ == "__main__":
    unittest.main()