def play_game(game_logic, game_description, max_rounds=3):

    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"\nHello, {name}!\n")
    print(game_description + "\n")

    for _ in range(max_rounds):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!\n")
            return

    print(f"Congratulations, {name}!")