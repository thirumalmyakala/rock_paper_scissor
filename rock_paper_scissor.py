import random
def play():

    user = input("Choice: 'r' for rock, 'p' for paper, 's' for scissor ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "its a tie"

    if is_win(user, computer):
       return 'you own'
    return "you lost"

        
def is_win(player, opponent):
    # r>s s>p p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())