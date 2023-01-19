from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Float, String, Boolean

Base = declarative_base()
engine = create_engine("sqlite:///hotelDB.db", echo=False)


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key = True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    gender = Column(String(255))
    days = Column(Integer)
    checked_in = Column(Boolean, default=True)

    def serialize_me(self):
        return f"""Customer Details for {self.first_name} {self.last_name}.
        Gender: {self.gender} Length of Stay: {self.days}
        Status: {'Checked In' if self.checked_in else 'Checked Out' }"""


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
