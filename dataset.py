from database import Country, State, Sight, Session

"""
 	Модуль для заполнения БД данными
"""

Russia=Country("Россия", 164_745_098 ,17_125_407)
USA=Country("США", 295_734_100, 9_976_140)
China=Country("Китай", 1_306_313_800, 9_629_091)
India=Country("Индия",1_080_264_400, 3_287_590)
Italy=Country("Италия", 58_103_000, 301_230)

Session.add_all([Russia,USA,China,India,Italy])
Session.commit()

Irkuts=State("Иркутская область", Russia)
SPB=State("Ленинградская область", Russia)
Arisona=State("Аризона", USA)
NewYork=State("Нью-Йорк", USA)
Chuauczhou=State("Хуайджоу", China)
Chenan=State("Хэнань", China)
Utar=State("Утар-Прадешь", India)
NewDaly=State("Нью Дели", India)
Neapol=State("Неаполь", Italy)
Venice=State("Венеция", Italy)

Session.add_all(
	[Irkuts,
	SPB,
	Arisona,
	NewYork,
	Chuauczhou,
	Chenan,
	Utar,
	NewDaly,
	Neapol,
	Venice])

Session.commit()

Baikal=Sight("Байкал", 1643, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo accusantium recusandae veniam earum dolorum non aperiam eaque, doloremque in labore, adipisci corrupti enim incidunt! Debitis magnam reiciendis, aliquam delectus quasi.", Irkuts)
Petergoph=Sight("Петергоф", 1710, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nam aperiam consectetur ab. Libero autem recusandae optio ut dolorum ad doloribus veniam, aspernatur voluptates quas delectus mollitia dolore hic eos accusantium!.", SPB)
BigCanion=Sight("Большой каньон", 1540, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolores, doloribus natus ratione nostrum veniam, nemo quaerat minima magnam nobis totam tempora quas culpa ab libero! Facere quo facilis error enim.", Arisona)
StatueOfLiberty=Sight("Статуя свободы", 1886, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eius, doloribus obcaecati. Atque libero, laboriosam odio labore minima ipsa, soluta corrupti perferendis enim tenetur omnis. Voluptates veniam fuga esse quidem ad.", NewYork)
TheGreatWallOfChina=Sight("Великая китайская стена", -300, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Harum perferendis, enim obcaecati optio quidem voluptatibus minus possimus aperiam, ducimus dolorum cum nesciunt corporis alias modi veritatis consequatur temporibus rerum iusto.", Chuauczhou)
SpringTepmleBuddhs=Sight("Статуя Будды", 2002, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis ut animi sapiente hic tenetur, maxime vel nisi unde dolorem, accusamus magni maiores pariatur quos expedita natus corporis quis corrupti et.", Chenan)
TarghMahal=Sight("Тардж махал", 1653, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Distinctio ea facere a reprehenderit aliquid. Inventore, modi at corrupti eligendi dolorem quaerat fugit veritatis cupiditate soluta quia blanditiis omnis optio assumenda?", Utar)
LotusTemple=Sight("Храм лотоса", 1986, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ullam quam esse, eos! Deleniti temporibus, harum nostrum voluptatem nulla a perspiciatis quibusdam, numquam quod obcaecati, atque itaque cumque rem, reprehenderit odio.", NewDaly)
Сolosseum=Sight("Колизей", 80, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda velit quis, ex iusto, nam molestias dolore quia asperiores alias obcaecati maiores consequatur qui porro natus totam commodi earum, odio itaque.", Neapol)
SaintMarko=Sight("пл.Святого Марка", 904, "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ea quibusdam consequuntur dignissimos quia similique incidunt tenetur cupiditate mollitia ex dolor, nostrum aspernatur tempora voluptatibus. Alias enim, ea sunt eligendi beatae.", Venice)

Session.add_all([Baikal,
	Petergoph,
	BigCanion,
	StatueOfLiberty,
	TheGreatWallOfChina,
	SpringTepmleBuddhs,
	TarghMahal,
	LotusTemple,
	Сolosseum,
	SaintMarko])
Session.commit()