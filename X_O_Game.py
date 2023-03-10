print(" Крестики-нолики для двоих. ", "\n", "Перед Вами игровое поле представленное в виде пронумерованых ячеек.",
      "\n", "Для осуществления хода выберете номер ячейки от 1 до 9.", "\n", "Пусть победит сильнейший! ")

playing_field = list(range(1, 10))

def draw_board(playing_field):
   print()
   print('', *playing_field[0:3], '\n', *playing_field[3:6], '\n', *playing_field[6:9])

def take_input(motion):
   check = True
   while check:
      print()
      player_answer = input("Вместо какого числа поставить " + motion+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(playing_field[player_answer-1]) not in "XO"):
            playing_field[player_answer-1] = motion
            check = False
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_winner(playing_field):
   winner_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in winner_coord:
       if playing_field[each[0]] == playing_field[each[1]] == playing_field[each[2]]:
          return playing_field[each[0]]
   return False

def main(playing_field):
    counter = 0
    winner = True
    while winner:
        draw_board(playing_field)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_winner(playing_field)
           if tmp:
              print(tmp, "выиграл!")
              win = False
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(playing_field)
main(playing_field)