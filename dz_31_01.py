from dataclasses import dataclass


@dataclass
class Book:
    name: str
    lastname: str
    marks: list[int]

    def summa_ballov(self):
        return sum(self.marks)


books = []
for line in open("marks.csv"):
    lastname, name, *marks = line.split(",")
    marks = list(map(int, marks))
    books.append(Book(name, lastname, marks))

for i in range(4):
    s = 0
    for book in books:
        s += book.marks[i]
    print(s / len(books))

maxi = 0
for book in books:
    if book.summa_ballov() > maxi:
        maxi = book.summa_ballov()
print(maxi)

"""
marks.csv

Александрова,Маргарита,3,3,4,2	
Алескеров,Имран,3,4,4,2		
Бармин,Владимир,4,3,4,2		
Барышев,Игорь,3,3,3,2		
Басова,Елена,4,4,4,2		
Блехман,Юлия,4,4,3,2		
Вишницкий,Илья,5,4,4,2		
Волхонская,Наталья,4,3,3,2		
Гатаулина,Алиса,3,3,4,2		
Грачёв,Артём,5,4,3,2		
Грицков,Илья,5,3,4,2		
Дергачёва,Анастасия,3,3,5,2		
Доброседов,Константин,4,3,4,2	
Долина,Валерия,3,5,2,2		
Дрогунова,Анастасия,3,3,4,2		
Емельяненко,Кирилл,5,4,4,2		
Жанайдаров,Даулет,5,4,5,2		
Зимин,Константин,3,5,3,2		
Зотова,Ольга,3,3,4,2		
Кобаненко,Глеб,4,2,3,2		
"""
