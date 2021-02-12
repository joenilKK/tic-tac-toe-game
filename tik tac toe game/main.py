import itertools
from os import system
from colorama import Fore, Back, Style, init

init()

#function check the winner
def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontally check winner
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # vertically check winner
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    # / diagonally check winner
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (/)")
        return True

    # \ diagonally check winnner
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (\\)")
        return True

    return False

#function for game mapping
def game_board(game_map, player=0, row=0, column=0, just_display=False):

    try:
        if game_map[row][column] != 0:
            print(f"This space is occupied by Player {current_player-1}, Enter other position")
            return False

        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
               game_map[row][column] = player

        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + " X " + Style.RESET_ALL
                elif item  == 2:
                    colored_row += Fore.MAGENTA + " O " + Style.RESET_ALL
            print(count, colored_row)
            
        return game_map
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False


play = True
players = [1, 2]

while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    player_cycle = itertools.cycle([1, 2])
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            try:
                if current_player == 1:
                    print("Player: " + Fore.GREEN + f"{current_player}" + Style.RESET_ALL )
                else:
                    print("Player: " + Fore.MAGENTA + f"{current_player}" + Style.RESET_ALL )
                column_choice = int(input("Which column? "))
                row_choice = int(input("Which row? "))
                system('cls')
                played = game_board(game, player=current_player, row=row_choice, column=column_choice)
            except ValueError:
                print("Invalid input, enter new!")
        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting!")
            elif again.lower() == "n":
                print("Thank youuu...")
                play = False
            else:
                print("Not a valid answer, but... c ya!")
                play = False