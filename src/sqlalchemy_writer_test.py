import unittest
from sqlalchemy_writer import SqlAlchemyWriter
from model.skill import Skill


class SqlAlchemyWriterTest(unittest.TestCase):
    def test_all(self):
        SqlAlchemyWriter().remove_skill(id='00001')
        SqlAlchemyWriter().remove_skill(id='00002')
        SqlAlchemyWriter().remove_skill(id='00003')

        SqlAlchemyWriter().add_skill(Skill(id='00001', name='python3'))
        SqlAlchemyWriter().add_skill(Skill(id='00002', name='java'))
        SqlAlchemyWriter().add_skill(Skill(id='00003', name='AWS'))

        SqlAlchemyWriter().update_skill(id='00001', name='python2')
        SqlAlchemyWriter().update_skill(id='00002', name='java1.8')


if __name__ == "__main__":
    unittest.main()