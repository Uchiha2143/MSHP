#МШП Чудес!


import random  # Для рандома
import time  # Для "остановки" времени


# Хранилище вопросов в программе

#Ключ -- вопрос
#Значение -- ответ (записываем только КАПСОМ)
a = random.randint(1,5)
b = "a"

if a == 1:
    b = "РОССИЯ"
    a = "Какая самая большая страна в нашем мире?"
    tasks = {
    a: b
    }
if a == 2:
    b = "ЕВРАЗИЯ"
    a = "На каком материке находится Россия?"
    tasks = {
    a: b
    }
if a == 3:
    b = "БАЙКАЛ"
    a = "Какое самое глубокое озеро в мире?"
    tasks = {
    a: b
    }
if a == 4:
    b = "ЭЛЬБРУС"
    a = "Какая самая высокая гора в России?"
    tasks = {
    a: b
    }
if a == 5:
    b = "ТИХИЙ"
    a = "Какой океан самый большой?"
    tasks = {
    a: b
    }

# Подсчёт очков
score = 0

# Секции барабана
drum_sectors = (100, 200, 300, 400, 500, 750, 1000, 2000, 5000, "💀", "Пропуск хода")
# Стрелка барабана
arrow = 0

# Случайный выбор вопроса

#1. Получаем ключи из словаря;
#2. Превращаем их в список ключй;
#3. Выбираем случайный ключ.

task = random.choice(list(tasks.keys()))
answer = tasks[task]

# Список букв, которые пытался угадать пользователь
true_letters = list()  # То, что использовали и оно подошло

# Выводим приветсвие
print("Загрузка.")
time.sleep(1)
print("Загрузка..")
time.sleep(1)
print("Загрузка...")
time.sleep(2)
print("／ﾌﾌ 　　　　　 　　 　ム｀ヽ")
print(" /ノ)　　 ∧　　∧　　　　）　ヽ")   
print("/ ｜　　(´・ω ・`）ノ⌒（ゝ._,ノ")
print("/　ﾉ⌒＿⌒ゝーく　 ＼　　／")
print("丶＿ ノ 　　 ノ､　　|　/")
print("   `ヽ `ー-‘人`ーﾉ /")
print("      丶 ￣ _人’彡ﾉ")
print("      ／｀ヽ _/\__'")
time.sleep(2)
print("...")
time.sleep(1.2)
print("Здравствуй дорогой друг!😗")
time.sleep(1.2)
print("Ты попал в телешоу 'МШП чудес'!🌚")
time.sleep(2)
print("Ваш вопрос в этой игре:")
time.sleep(2)
print(task)
time.sleep(3) 

# Игровой цикл
answer_letters = set(answer)  # Множество правильных букв
while len(true_letters) != len(answer_letters):
    
    #1. Перебираем все буквы в ответе;
    #2. Если пользователь уже называл правильную букву -- добавляем её в список;
    #3. Иначе -- добавляем вместо неё символ '⬛';
    #4. Выводим список.
    
    print(*[letter if letter in true_letters else '🟪' for letter in answer])
    print('-' * 180)  # Просто красивая полосочка
    print("Введите 1, чтобы прокрутить барабан🔥, либо назовите ответ целиком (КАПСОМ!)")
    user_input = input()
    if user_input == '1':  # Тут крутим барабан
        drum_force = random.randint(3, 10)  # Сколько ячеек прокрутим
        for _ in range(drum_force):  # Крутим барабан
            
            #1. Крутим стрелку на 1;
            #2. Не выходим за границы списка.
            
            arrow = (arrow + 1) % len(drum_sectors)
            drum_sector_choice = drum_sectors[arrow]  # Что выпало на этом вращении
            print('\r', drum_sector_choice, ' ' * 10, end='')
            # Этак команда ставит выполнение кода на паузу на 0.15 секунды (чтобы у нас барабан не крутился мгновенно)
            time.sleep(0.15)#Вот количество твоих очков
        if drum_sector_choice == "💀":
            print("Тебе выпал сектор с черепом, это автоматический проигрыш!")
            time.sleep(1) 
            print("Ты проиграл, у тебя 0 очков..")
            time.sleep(1) 
            print("Если хотите сыграть еще раз, запустите программу заново.")
            break
        elif drum_sector_choice == "Пропуск хода":
            print("Тебе выпал сектор 'пропуск хода'!")
            time.sleep(1) 
            print("Ты пропускаешь ход!")
        else:
            score += drum_sector_choice
            print("Введите букву (КАПСОМ!):")
            user_letter = input()
            if user_letter in answer:
                if user_letter in true_letters:
                    print("Эта буква уже была...")
                else:
                    true_letters.append(user_letter)
    
    elif user_input == answer:
        print("Вы становитесь победителем телешоу 'МШП чудес'")
        time.sleep(1) 
        print("Ты победил, весь твой счет превращается в деньги💲💲💲!!")
        time.sleep(1) 
        print("Твой счёт -", score)
        break
    else:
        print("Ты проиграл(, слово было", answer)
        time.sleep(1) 
        print("Твой счёт - 0")
        break

if len(true_letters) == len(answer_letters):
    print("Победил")
    time.sleep(1) 
    print("Твой счёт", score)
