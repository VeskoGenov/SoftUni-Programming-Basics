failed_exercises = int(input())

exercise_count = 0
exercise_vote_count = 0
failed_vote = 0
last_exercise = ""

while failed_vote < failed_exercises:
    exercise_name = input()

    if exercise_name == "Enough":
        print(f"Average score: {exercise_vote_count / exercise_count:.2f}")
        print(f"Number of problems: {exercise_count}")
        print(f"Last problem: {last_exercise}")
        break

    vote = int(input())

    if vote <= 4:
        failed_vote += 1
    if failed_vote == failed_exercises:
        print(f"You need a break, {failed_vote} poor grades.")
        break

    exercise_count += 1
    exercise_vote_count += vote
    last_exercise = exercise_name