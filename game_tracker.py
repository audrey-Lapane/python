#An interactive program that continuously asks an arcade player for their game score.


while True:
    game_score = input("Enter your game score next to the flashing cursor:").strip().lower()

    if game_score == "stop": 
        print("Game session ended!")
        break
    else:
        score = int(game_score)
        if score > 100:
            print("Wow! That's a new high score")

        else:
            print("Good try, keep playing!")


