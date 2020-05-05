from sqlalchemy import create_engine, Column, Integer,\
					 String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base=declarative_base()

#Создаем базу данных sqlite в оперативной памяти компьютера
engine=create_engine('sqlite:///:memory:') 

#Сессия соединения с базой данных
Session=sessionmaker(bind=engine)()


#Модель стран мира
class Country(Base):
	"""
		Модель содержит имформацию о странах мира
	"""
	__tablename__='countries'
	countryId=Column(Integer, primary_key=True)
	name=Column(String, nullable=False, unique=True) 				# Название страны
	population=Column(Integer)		# Население
	area=Column(Float)				#Площадь 
	states=relationship("State", cascade="all, delete-orphan")		#Список областей		

	def __init__(self, name, population,area):
		self.name=name
		self.population=population
		self.area=area

class State(Base):
	"""
		Модель содержит информацию о регионе в котором находится достопримечательность
	"""
	__tablename__='states'
	stateId=Column(Integer, primary_key=True) 
	name=Column(String,nullable=False, unique=True) #Название области/края/республики/штата/города
	countryId=Column(Integer, ForeignKey('countries.countryId'))

	country=relationship('Country', backref='countries', cascade="all,delete")
	sights=relationship("Sight", cascade="all, delete-orphan")

	def __init__(self, name, country):
		self.name=name
		self.countryId=country.countryId

class Sight(Base):
	"""
		Модель содержит информацию о достопримечательнотях в регионе

	"""
	__tablename__='sights'
	sightId=Column(Integer, primary_key=True)
	name=Column(String,nullable=False, unique=True) #Название достопримечательности
	year=Column(Integer) #Год постройки иили обнаружения(В случае природного происхождения)
	description=Column(String) #Описание достопремичательности
	stateId=Column(Integer, ForeignKey('states.stateId'))
	state=relationship('State', backref='states', cascade="all,delete")

	def __init__(self, name, year, description, state):
		self.name=name
		self.year=year
		self.description=description
		self.stateId=state.stateId


Base.metadata.create_all(engine)
