from database import Country, State, Sight, Session

import dataset #Закомментировать данный импорт, если создается файл БД, а не в опретивной памяти

def printSights():
	#Вывод данных
	data=Session.query(Sight)
	
	for row in data:
		print("\"{}\" год: {} Область: {} Страна: {}".format(row.name,row.year, row.state.name, row.state.country.name))

if __name__ == '__main__':

	print("Вывод достопримечательностей\n")
	printSights()
	

	#Добавление данных
	Russia=Session.query(Country).filter(Country.name=="Россия").one()
	Volgograd=State("Волгоградсткая Область", Russia)
	Session.add(Volgograd)
	Session.commit()
	newSigt=Sight("Родина-Мать", 1967, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda velit quis, ex iusto, nam molestias dolore quia asperiores alias obcaecati maiores consequatur qui porro natus totam commodi earum, odio itaque.", Volgograd)
	Session.add(newSigt)
	Session.commit()
	print()
	print("Добавлены данные\nДостопримечательность: Родина-Мать")
	printSights()

	#Каскадное удаление данных
	USA=Session.query(Country).filter(Country.name=="США").one()
	Session.delete(USA)
	Session.commit()
	print()
	print("Каскадное удаление данных\n")
	printSights()
	print("\nСША и все её достопримечательности удалены успешно")
