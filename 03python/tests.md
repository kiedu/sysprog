# Python3

## Test #1: Python3. Структури даних
https://forms.gle/8e5NTmk4gwX3sD8N9?authuser=0


### Що виведе цей код на Python?
```
stuff = dict()
print(stuff['candy'])
```
* candy
* -1
* 0
* програма завершиться помилкою


### Як би ви вивели вміст змінної greet у верхньому регістрі на Python?
```
greet = 'Hello Bob'
```
* print(greet.upper())
* puts(greet.ucase);
* print(uc($greet));
* console.log(greet.toUpperCase());


### Який з наведених методів роботи з рядками видаляє пробіли як з початку, так і в кінці рядка?

* wsrem()
* strtrunc()
* rltrim()
* strip()

### Яка змінна є ітераційною у такому коді на Python?
```
for letter in 'banana':
    print(letter)
```
* for
* letter
* 'banana'
* in
* print


### Що виведе ця програма на Python?
```
x = '40'
y = int(x) + 2
print(y)
```
* 42
* 402
* int402
* x2


### Яка різниця між кортежем і списком у Python?
* Кортежі можна розширювати після створення, а списки - ні.
* Списки індексуються цілими числами, а кортежі - рядками.
* Списки зберігають порядок елементів, а кортежі не зберігають порядок.
* Списки змінювані, а кортежі ні.


### Що виведе ця програма на Python?
```
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)
```
* Hello there
* Hellothere
* Hello
* 0


### Який з наведених рядків Python еквівалентний наступній послідовності операторів, якщо припустити, що counts є словником?
```
if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1
```
* counts[key] = (counts[key] * 1) + 1
* counts[key] = (key in counts) + 1
* counts[key] = key + 1
* counts[key] = counts.get(key,-1) + 1
* counts[key] = counts.get(key,0) + 1


### Чому у цьому циклі Python дві ітераційні змінні (k та v)?
```
c = {'a':10, 'b':1, 'c':22}
for k, v in c.items() :
    ... 
```
* Тому що в словнику є два елементи
* Тому що метод items() у словниках повертає ключ та значення
* Тому що ключі для словника є рядками
* Тому що для кожного елементу нам потрібен попередній та поточний ключ


### Що виводить такий код на Python?
```
print(len('banana')*7)
```
* bananabananabananabananabananabananabanana
* banana7
* 0
* 42


### Що виводить цей код на Python?
```
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))
```
* [1, 2, 3]
* [4, 5, 6]
* 21
* 15
* [1, 2, 3, 4, 5, 6]
* 6



### Яке призначення цього коду на Python?
```
fhand = open('mbox.txt')
x = 0
for line in fhand:
       x = x + 1
print(x)
```
* Змінити порядок рядків у файлі mbox.txt на протилежний
* Видалити початковий і кінцевий пробіли з кожного рядка в mbox.txt
* Перетворити рядки в mbox.txt в нижній регістр
* Підрахувати кількість рядків у файлі mbox.txt


### Які ключові слова Python використовуються для побудови циклу для ітерації по списку?

* foreach / in
* def / return
* for / in
* try / except


### Що робить цей код на Python?
```
fhand = open('mbox-short.txt')
inp = fhand.read()
```
* Перевіряє, чи існує файл і чи можна до нього щось записати
* Читає перший рядок файлу у змінну inp
* Читає весь файл у змінну inp
* Запропонує користувачеві ввести ім'я файлу


### Що виведе цей код на Python?
```
stuff = dict()
print(stuff.get('candy',-1))
```
* -1
* candy
* програма завершиться помилкою
* 0



### Що буде у змінній y після виконання цього коду?
```
x, y = 3, 4
```
* Словник з ключем 3, який зіставляється зі значенням 4
* 3
* Кортеж з двох елементів
* Список з двох елементів
* 4


### Яка з наведених інструкцій Python виведе довжину списку, що зберігається у змінній data?
* print(length(data))
* print(strlen(data))
* print(len(data))
* print(data.length)
* print(data.Len)
* print(data.length())


### Що виведе цей код на Python?
```
fruit = 'Banana'
fruit[0] = 'b'
print(fruit)
```
* Нічого - програма поверне помилку
* b
* [0]
* B
* banana
* Banana


### Використовуючи наведений кортеж, як би ви вивели 'Wed'?
```
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun') 
```
* print(days[1])
* print(days(2))
* print(days[2])
* print[days(2)]
* print(days.get(1,-1))
* print(days{2})


### Як би ви вивели «Sally» з такого списку?
```
friends = ['Joseph', 'Glenn', 'Sally']
```
* print(friends[2])
* print(friends['Sally'])
* print friends[3]
* print(friends[2:1])


