#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def mysqlconnect(username, password, database, port=3306):
    """
    Function:
        Connect to MySQL with sqlalchemy.
    Args:
        username (str): username to connect to MySQL.
        password (str): password to connect to MySQL.
        database (str): database to connect to MySQL.
        port (int): port to connect to MySQL.
    Return:
        Connect to MySQL (session) use sqlalchemy.
    """
    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost:{}/{}'.format(
                            username,
                            password,
                            port,
                            database),
                    pool_pre_ping=True)
    bd_session = sessionmaker(bind=engine)
    return bd_session()


if __name__ == '__main__':
    bd_session = mysqlconnect(sys.argv[1], sys.argv[2], sys.argv[3])
    states = bd_session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        bd_session.delete(state)

    bd_session.commit()
