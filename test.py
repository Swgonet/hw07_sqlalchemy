from sqlalchemy import engine
from my_select import session
from models import Base

Base.metadata.drop_all(engine.drop_all(), checkfirst=True)

session.commit()