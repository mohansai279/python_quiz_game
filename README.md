# python_quiz_game
The Quiz Game project is a command-line application designed to test users' knowledge of Object-Oriented Programming (OOP) concepts through a series of multiple-choice questions. The game provides immediate feedback on user responses, tracks scores, and displays the final results at the end of the quiz.
## Usage

Run the program using Python:

```bash
python 10.Quiz_game_project.py
```

Follow the prompts to answer the quiz questions. Enjoy testing your knowledge!

## Detailed Logic Breakdown

### Step 1: Constructing the Quiz Content: The Data Layer

- **question_bank (The Questions and Answers)**:
  - A list of dictionaries where each dictionary represents a question with its text and correct answer.

- **options (The Multiple-Choice Options)**:
  - A parallel list of lists that corresponds to the questions in `question_bank`. Each sublist contains the multiple-choice options for the respective question.

- **score**:
  - An integer variable initialized to zero, used to track the player's score throughout the game.

### Step 2: A Simple, Reusable Tool: The check_answer Function

- **check_answer(user_guess, correct_answer)**:
  - This function compares the user's guess to the correct answer, returning `True` if they match and `False` otherwise. This encapsulation promotes code readability and modularity.

### Step 3: The Quiz Engine: The Main for Loop

- The main loop iterates through each question, handling user interaction and updating the game state:
  
  ```python
  for question_num in range(len(question_bank)):
  ```

- **Displaying Questions and Options**:
  - Each question and its corresponding options are displayed using the index to access the appropriate elements from `question_bank` and `options`.

- **Getting User Input**:
  - The user's input is captured and converted to uppercase to ensure case insensitivity.

- **Evaluating Answers**:
  - The user's guess is checked using `check_answer(...)`, and feedback is provided based on the outcome. The score is updated accordingly.

- **Live Score Tracking**:
  - The current score is displayed after each question, providing real-time feedback.

### Step 4: The Final Tally: Displaying the Results

- Once all questions have been answered, the program displays the user's final score and percentage:

  ```python
  print(f"Your Final score is {score}")
  print(f"Your score is {(score / len(question_bank)) * 100}%")
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
