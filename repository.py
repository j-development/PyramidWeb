from datetime import datetime

from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, session

Base = declarative_base()


class CarModel(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True)
    maker = Column(String(16), nullable=False)
    model = Column(String(16), nullable=False)
    color = Column(String(16), nullable=False)
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def car_model(self):
        return f'{self.maker} {self.model}'

    def __repr__(self):
        return (
            f'Car(id={self.id}, ={self.maker},'
            f'model={self.model}, color={self.color},'
            f'created={self.created})'
        )


cars = [
    CarModel(maker='Volvo', model='S60', color='Black'),
    CarModel(maker='Lamborghini', model='Huracan', color='Orange'),
    CarModel(maker='Ferrari', model='F548', color='Red'),
]

session_maker = sessionmaker(bind=create_engine('mysql://root:blackmesa@localhost:3306/pyramidDB'))


def create_cars():
    with session_maker() as sess:
        for car in cars:
            sess.add(car)
        sess.commit()


# create_cars()


def get_cars():
    with session_maker() as sess:
        result = []
        car_records = sess.query(CarModel).all()
        for car in car_records:
            result.append(car)
        return result


