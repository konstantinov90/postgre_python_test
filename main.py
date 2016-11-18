from sqlalchemy import create_engine  # начните работу с этой библиотеки
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

from User import User


db_conn_string = 'postgresql://postgres:123456@localhost/postgres'

engine = create_engine(db_conn_string, echo=False)

metadata = MetaData()
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(50)),
                    Column('fullname', String(50)),
                    Column('password', String(50))
                    )

# metadata.create_all(engine)

mapper(User, users_table)

# user = User('Вася', 'Василий', 'qwerty')
# print(user)
# print(user.id)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
# session.add(user)

ourUser = session.query(User).filter_by(name="Вася").first()
ourUser.password = 'new_pass'
print(ourUser, ourUser.id)
