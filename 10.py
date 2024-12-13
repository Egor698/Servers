import random

#переменные
banList = []

class plaeyrClas:
   banGet = False
   statusGet = "Игрок"
   onlain = True

player = plaeyrClas()
banGet = False
statusGet = "Игрок"
onlain = True

#функции
def tp():
       x = random.randint(1000, 10000)
       y = random.randint(12, 55)
       z = random.randint(1000, 10000)
       print(f"Вы перемещенны на координаты x {x},y {y},z {z}")

def chat():
    input()


while True:

 try:
  comandMsgGet = input()
  if comandMsgGet == "/chekban":
       if player.banGet == False:
          print("Бан отсутствует")
       else:
          print("Вам был выдан бан")
  elif comandMsgGet == "/help":
      print("Доступные команды:\n/chekban - проверяет есть ли бан\n/chekstatus - проверяет на привелегию\n/tp - выдает рандомные кординаты\n/cheklain - проверяет онлайн")

  elif comandMsgGet == "/chekstatus":
          print(f"Ваша привелегия: {player.statusGet}")

  elif comandMsgGet == "/tp":
         tp()

  elif comandMsgGet == "/cheklain":
      if player.onlain == True:
          print("Пользователь онлайн")
      else:
          print("Пользователь не онлайн")

  elif comandMsgGet == "@" and "/getadmin":
      player.statusGet = "Админ"
      print("Игроку @ выдан статус")

 except ValueError:
     chat()




         
         
         
            
