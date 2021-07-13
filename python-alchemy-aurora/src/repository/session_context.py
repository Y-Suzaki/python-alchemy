import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session


class SessionContext:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.session_maker = sessionmaker(bind=self.create_aurora_engine(), expire_on_commit=False)

    class Session:
        def __init__(self, session_maker):
            print('init')
            self.session: Session = session_maker()

        def __enter__(self):
            print('enter')
            return self.session

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                print('rollback')
                self.session.rollback()
            else:
                print('commit')
                self.session.commit()

            self.session.close()
            print('exit')

    def create_aurora_engine(self):
        db_arn = os.environ['DB_ARN']
        db_secret_arn = os.environ['DB_SECRET_ARN']

        return create_engine(f'mysql+auroradataapi://:@/{self.db_name}',
                             echo=True,
                             connect_args=dict(aurora_cluster_arn=db_arn, secret_arn=db_secret_arn))

    def make(self):
        return self.Session(self.session_maker)
