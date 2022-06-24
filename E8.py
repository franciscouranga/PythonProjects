def enter_vote(n):

    while True:
        inp = str(input("ROCK, PAPER, SCISSORS PLAYER " + str(n) + ": "))
        if inp in ["r", "p", "s"]:
            break
        else:
            print("Enter a valid character.")
    return inp


def comparison_rps(inp1, inp2):

    if (inp1 == "r" and inp2 == "s") or (inp1 == "p" and inp2 == "r") or (inp1 == "s" and inp2 == "p"):
        w = 1
    elif (inp1 == "s" and inp2 == "r") or (inp1 == "r" and inp2 == "p") or (inp1 == "p" and inp2 == "s"):
        w = 2
    else:
        w = 0
    return w


if __name__ == "__main__":
    print("Rock, paper, scissors game. \nPress \"r\" for rock, \"p\" for paper and \"s\" for scissors.")
    win = 0
    while win == 0:
        inp1 = enter_vote(1)
        inp2 = enter_vote(2)
        win = comparison_rps(inp1, inp2)
        if win == 0:
            win = input("There is a draw! Do you want to play again? (y/n) ")
            if win in ["y", "yes", "ye"]:
                win = 0

    if win == 1:
        print("Player 1 wins!")
    elif win == 2:
        print("Player 2 wins!")
    else:
        print("There is no winner!")
