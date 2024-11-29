import json
import customtkinter
import random

with open("users.json", "r") as f:
    userFile = json.loads(f.read())

#Essential functions, used numerous times

def saveUserData():
    with open("users.json", "w") as f:
        saveData = json.dumps(userFile, indent=4)
        f.write(saveData)

def clearScreen(root): #Subroutine used to clear the screen so new elements can be added
    for i in root.winfo_children():
        i.destroy()

#Main menu funtion

def mainMenu(root, currentUser):

    clearScreen(root)

    mainTitle = customtkinter.CTkLabel(root, text="MAIN MENU", font=("Arial", 30))
    mainTitle.pack(pady=10)

    quizButton = customtkinter.CTkButton(root, text="Take a quiz", cursor="hand2", font=("Arial", 18), command=lambda: quizMenu(root, currentUser))
    quizButton.pack(pady=10)

    profileButton = customtkinter.CTkButton(root, text="View Profile", cursor="hand2", font=("Arial", 18), command=lambda: viewProfile(root, currentUser))
    profileButton.pack(pady=10)

    quizInfoButton = customtkinter.CTkButton(root, text="Quiz Information", cursor="hand2", font=("Arial", 18), command=lambda: quizInfo(root, currentUser))
    quizInfoButton.pack(pady=10)

    difficultyInfoButton = customtkinter.CTkButton(root, text="Difficulty Information", cursor="hand2", font=("Arial", 18), command=lambda: difficultyInfo(root, currentUser))
    difficultyInfoButton.pack(pady=10)

    quitButton = customtkinter.CTkButton(root, text="Quit", command=root.destroy, cursor="hand2", font=("Arial", 18))
    quitButton.pack(pady=10)

#Functions used for seeing the difficulty information

def difficultyInfo(root, currentUser):
    
    clearScreen(root)

    mainTitle = customtkinter.CTkLabel(root, text="DIFFICULTY INFORMATION", font=("Arial", 30))
    mainTitle.pack(pady=10)

    selectLabel = customtkinter.CTkLabel(root, text="Select a difficulty:", font=("Arial", 18))
    selectLabel.pack(pady=10)

    easyButton = customtkinter.CTkButton(root, text="Easy", cursor="hand2", font=("Arial", 18), command=lambda: getDifficultyInfo(root, currentUser, "easy"))
    easyButton.pack(pady=10)

    mediumButton = customtkinter.CTkButton(root, text="Medium", cursor="hand2", font=("Arial", 18), command=lambda: getDifficultyInfo(root, currentUser, "medium"))
    mediumButton.pack(pady=10)

    hardButton = customtkinter.CTkButton(root, text="Hard", cursor="hand2", font=("Arial", 18), command=lambda: getDifficultyInfo(root, currentUser, "hard"))
    hardButton.pack(pady=10)

    backButton = customtkinter.CTkButton(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    backButton.pack(pady=10)

def getDifficultyInfo(root, currentUser, difficulty):

    clearScreen(root)

    mainTitle = customtkinter.CTkLabel(root, text="DIFFICULTY INFORMATION", font=("Arial", 30))
    mainTitle.pack(pady=10)

    numberQuizzesTaken = 0
    totalScore = 0
    bestScore = 0
    bestScorer = ""
    
    for user, userDetails in userFile.items():
        for quiz in userDetails["quizzes"].values():
            if quiz["quizDifficulty"] == difficulty:
                numberQuizzesTaken += 1
                totalScore += quiz["quizScore"]
                if quiz["quizScore"] > bestScore:
                    bestScore = quiz["quizScore"]
                    bestScorer = user

    if numberQuizzesTaken > 0:

        quizzesLabel = customtkinter.CTkLabel(root, text=f"Number of {difficulty} quizzes taken: {numberQuizzesTaken}", font=("Arial", 18))
        quizzesLabel.pack(pady=10)

        averageScoreLabel = customtkinter.CTkLabel(root, text=f"Average score: {round(totalScore / numberQuizzesTaken, 2)}/5", font=("Arial", 18))
        averageScoreLabel.pack(pady=10)

        highestScoreLabel = customtkinter.CTkLabel(root, text=f"Best score: {bestScore}/5", font=("Arial", 18))
        highestScoreLabel.pack(pady=10)

        bestScorerLabel = customtkinter.CTkLabel(root, text=f"Best score achieved by: {bestScorer}", font=("Arial", 18))
        bestScorerLabel.pack(pady=10)

        backButton = customtkinter.CTkButton(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
        backButton.pack(pady=10)

    else:

        noneTakenLabel = customtkinter.CTkLabel(root, text=f"There have been no tests taken of this difficulty so far.", font=("Arial", 18))
        noneTakenLabel.pack(pady=10)

        backButton = customtkinter.CTkButton(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
        backButton.pack(pady=10)

#Functions used for seeing the quiz information

def quizInfo(root, currentUser):

    clearScreen(root)

    mainTitle = customtkinter.CTkLabel(root, text="QUIZ INFORMATION", font=("Arial", 30))
    mainTitle.pack(pady=10)

    usernameEntry = customtkinter.CTkEntry(root, placeholder_text="Enter a username")
    usernameEntry.pack(pady=10)

    statusMessage = customtkinter.CTkLabel(root, text="", font=("Arial", 18), text_color="red")
    statusMessage.pack(pady=10)

    submitButton = customtkinter.CTkButton(root, text="Submit", cursor="hand2", font=("Arial", 18), command=lambda: getQuizInfo(root, currentUser, usernameEntry.get(), statusMessage))
    submitButton.pack(pady=10)

    backButton = customtkinter.CTkButton(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    backButton.pack(pady=10)

def getQuizInfo(root, currentUser, usernameEntry, statusMessage):
    
    if usernameEntry not in userFile:
        statusMessage.configure(text="You did not enter in a valid username. Please try again.")

    else:

        clearScreen(root)

        mainTitle = customtkinter.CTkLabel(root, text=f"{userFile[usernameEntry]['username']}'s Quizzes", font=("Arial", 30))
        mainTitle.pack(pady=10)

        quizzesLabel = customtkinter.CTkLabel(root, text=f"Number of quizzes taken: {userFile[currentUser]['quizzesTaken']}", font=("Arial", 18))
        quizzesLabel.pack(pady=10)

        quizFrame = customtkinter.CTkScrollableFrame(root)

        index = 0

        for quiz, value in userFile[currentUser]["quizzes"].items():
            quizInfoLabel = customtkinter.CTkLabel(quizFrame, text=f"{quiz}: Grade: {value['quizGrade']}, Difficulty: {value['quizDifficulty']}")
            quizInfoLabel.grid(row=index, column=0, pady=5)
            index += 1

        quizFrame.pack(pady=10)

        backButton = customtkinter.CTkButton(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
        backButton.pack(pady=10)

#Function used for viewing the user profile

def viewProfile(root, currentUser):
    
    clearScreen(root)

    mainTitle = customtkinter.CTkLabel(root, text="VIEW PROFILE", font=("Arial", 30))
    mainTitle.pack(pady=10)

    usernameLabel = customtkinter.CTkLabel(root, text=f"Username: {currentUser}", font=("Arial", 18))
    usernameLabel.pack(pady=10)

    realNameLabel = customtkinter.CTkLabel(root, text=f"Name: {userFile[currentUser]['realName']}", font=("Arial", 18))
    realNameLabel.pack(pady=10)

    ageLabel = customtkinter.CTkLabel(root, text=f"Age: {userFile[currentUser]['age']}", font=("Arial", 18))
    ageLabel.pack(pady=10)

    quizzesLabel = customtkinter.CTkLabel(root, text=f"Number of quizzes taken: {userFile[currentUser]['quizzesTaken']}", font=("Arial", 18))
    quizzesLabel.pack(pady=10)

    moreInfoLabel = customtkinter.CTkLabel(root, text=f"To view more information about a specific users quizzes, use the Quiz Information button in the main menu.", font=("Arial", 18))
    moreInfoLabel.pack(pady=10)

    backButton = customtkinter.CTkButton(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    backButton.pack(pady=10)

#Functions used for the user taking the quiz

def quizMenu(root, currentUser):

    clearScreen(root)

    mainTitle = customtkinter.CTkLabel(root, text="QUIZZES", font=("Arial", 30))
    mainTitle.pack(pady=10)

    selectLabel = customtkinter.CTkLabel(root, text="Select a difficulty:", font=("Arial", 18))
    selectLabel.pack(pady=10)

    easyButton = customtkinter.CTkButton(root, text="Easy", cursor="hand2", font=("Arial", 18), command=lambda: generateQuiz(root, currentUser, "easy", 2))
    easyButton.pack(pady=10)

    mediumButton = customtkinter.CTkButton(root, text="Medium", cursor="hand2", font=("Arial", 18), command=lambda: generateQuiz(root, currentUser, "medium", 3))
    mediumButton.pack(pady=10)

    hardButton = customtkinter.CTkButton(root, text="Hard", cursor="hand2", font=("Arial", 18), command=lambda: generateQuiz(root, currentUser, "hard", 4))
    hardButton.pack(pady=10)

    backButton = customtkinter.CTkButton(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
    backButton.pack(pady=10)

def generateQuiz(root, currentUser, difficulty, options):

    with open("mathsquestions.json", "r") as f:
        questionsList = json.loads(f.read())
    
    difficultyQuestions = questionsList[difficulty]
    questions = random.sample(list(difficultyQuestions.items()), 5) #Takes 5 random questions from the mathsquestions.json file of the specified difficulty

    currentQuestion = 0
    correctAnswers = 0
    incorrectAnswers = 0

    def displayQuestion(progress):
        nonlocal currentQuestion

        if progress is True and currentQuestion < len(questions):
            question, questionInfo = questions[currentQuestion]

            clearScreen(root)

            mainTitle = customtkinter.CTkLabel(root, text=f"{difficulty.upper()} QUIZ", font=("Arial", 30))
            mainTitle.pack(pady=10)

            questionLabel = customtkinter.CTkLabel(root, text=f"Question {currentQuestion + 1}: {questionInfo[0]}", font=("Arial", 20))
            questionLabel.pack(pady=10)

            questionOptions = [questionInfo[1]]

            for _ in range(1, options):
                questionOptions.append(questionInfo[1] + random.randint(1, 50))

            random.shuffle(questionOptions)

            radio_var = customtkinter.StringVar()

            for option in questionOptions:
                optionButton = customtkinter.CTkRadioButton(root, text=f"{option}", value=option, variable=radio_var)
                optionButton.pack(pady=10)

            statusMessage = customtkinter.CTkLabel(root, text="", font=("Arial", 18), text_color="red")
            statusMessage.pack(pady=10)

            submitButton = customtkinter.CTkButton(root, text="Submit", cursor="hand2", font=("Arial", 18), command=lambda: processResult(radio_var.get(), questionInfo[1], statusMessage))
            submitButton.pack(pady=10)

    def processResult(userAnswer, correctAnswer, statusMessage):
        nonlocal currentQuestion, correctAnswers, incorrectAnswers
        if userAnswer:
            if userAnswer == str(correctAnswer):
                correctAnswers += 1
            else:
                incorrectAnswers += 1
            currentQuestion += 1
            if currentQuestion == 5:
                resultScreen()
                return
            displayQuestion(True)
        else:
            statusMessage.configure(text="You did not select a valid option. Please try again.")
            displayQuestion(False)

    def calculateGrade(correctAnswers):
        if correctAnswers == 5:
            return "A*"
        elif correctAnswers == 4:
            return "A"
        elif correctAnswers == 3:
            return "B"
        elif correctAnswers == 2:
            return "C"
        elif correctAnswers == 1:
            return "D"
        else:
            return "F"

    def resultScreen():
        nonlocal correctAnswers, difficulty, currentUser

        clearScreen(root)

        scoreLabel = customtkinter.CTkLabel(root, text=f"Score: {correctAnswers}/5", font=("Arial", 18))
        scoreLabel.pack(pady=10)

        percentageLabel = customtkinter.CTkLabel(root, text=f"Percentage: {round((correctAnswers/5) * 100)}", font=("Arial", 18))
        percentageLabel.pack(pady=10)

        grade = calculateGrade(correctAnswers)

        gradeLabel = customtkinter.CTkLabel(root, text=f"Grade: {grade}", font=("Arial", 18))
        gradeLabel.pack(pady=10)

        quizName = "quiz"
        uniqueQuiz = False
        index = 1

        while uniqueQuiz is False: #While loop to create a unique quiz name
            quizName = f"{quizName}{index}"
            if quizName in userFile[currentUser]["quizzes"]:
                index += 1
                quizName = "quiz"
            else:
                uniqueQuiz = True

        userFile[currentUser]["quizzes"].update({quizName: {
            "quizDifficulty": difficulty,
            "quizScore": correctAnswers,
            "quizGrade": grade
        }})

        userFile[currentUser]["quizzesTaken"] += 1

        quizName = "quiz" #Resets the quiz name in case they decide to take another quiz, so a new name can be generated

        saveUserData()

        backButton = customtkinter.CTkButton(root, text="Return to main menu", cursor="hand2", font=("Arial", 18), command=lambda: mainMenu(root, currentUser))
        backButton.pack(pady=10)

    displayQuestion(True)

#Functions used for the user login

def loginScreen(root):

    clearScreen(root)

    mainTitle = customtkinter.CTkLabel(root, text="USER LOGIN", font=("Arial", 30))
    mainTitle.pack(pady=10)

    usernameEntry = customtkinter.CTkEntry(root, placeholder_text="Username")
    usernameEntry.pack(pady=10)

    passwordEntry = customtkinter.CTkEntry(root, placeholder_text="Password", show="*")
    passwordEntry.pack(pady=10)

    statusMessage = customtkinter.CTkLabel(root, text="", font=("Arial", 18), text_color="red")
    statusMessage.pack(pady=10)

    loginButton = customtkinter.CTkButton(root, text="Log In", cursor="hand2", font=("Arial", 18), command=lambda: userLogin(usernameEntry.get(), passwordEntry.get(), statusMessage, root))
    loginButton.pack(pady=10)

    backButton = customtkinter.CTkButton(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: main(root))
    backButton.pack(pady=10)

def userLogin(username, password, statusMessage, root):

    if not username in userFile:
        statusMessage.configure(text="The username you entered does not exist. Please try again.")

    elif userFile[username]["password"] != password:
        statusMessage.configure(text="The password you entered is incorrect. Please try again.")

    else:
        statusMessage.configure(text="Logging in...")
        mainMenu(root, username)

#Functions used for signing up the user

def signUpScreen(root):

    clearScreen(root)

    mainTitle = customtkinter.CTkLabel(root, text="USER REGISTRATION", font=("Arial", 30))
    mainTitle.pack(pady=10)

    nameEntry = customtkinter.CTkEntry(root, placeholder_text="Name")
    nameEntry.pack(pady=10)

    passwordEntry = customtkinter.CTkEntry(root, placeholder_text="Password", show="*")
    passwordEntry.pack(pady=10)

    confirmEntry = customtkinter.CTkEntry(root, placeholder_text="Re-enter password", show="*")
    confirmEntry.pack(pady=10)

    ageEntry = customtkinter.CTkEntry(root, placeholder_text="Age")
    ageEntry.pack(pady=10)

    statusMessage = customtkinter.CTkLabel(root, text="", font=("Arial", 18), text_color="red")
    statusMessage.pack(pady=10)

    signupButton = customtkinter.CTkButton(root, text="Sign Up", cursor="hand2", font=("Arial", 18), command=lambda: userRegistration(nameEntry.get(), passwordEntry.get(), confirmEntry.get(), ageEntry.get(), statusMessage, root))
    signupButton.pack(pady=10)

    backButton = customtkinter.CTkButton(root, text="Go Back", cursor="hand2", font=("Arial", 18), command=lambda: main(root))
    backButton.pack(pady=10)

def userRegistration(realName, inputPassword, confirmPassword, userAge, statusMessage, root):
    
    if any(char.isdigit() for char in realName):
        statusMessage.configure(text="The name you entered contains numbers. Please try again.")
    elif not realName.isalnum():
        statusMessage.configure(text="The name you entered contains symbols or other disallowed characters. Please try again.")
    
    elif " " in inputPassword:
        statusMessage.configure(text="The password you entered contains a spacebar. Please try again.")
    elif len(inputPassword) < 8:
        statusMessage.configure(text="The password you entered is shorter than 8 characters. Please try again.")
    elif len(inputPassword) > 50:
        statusMessage.configure(text="The password you entered is longer than 50 characters. Please try again.")

    elif inputPassword != confirmPassword:
        statusMessage.configure(text="The passwords you entered do not match. Please try again.")

    elif not userAge.isnumeric():
        statusMessage.configure(text="The age that you entered in is not in numbers. Please try again.")
    elif int(userAge) > 120 or int(userAge) < 0:
        statusMessage.configure(text="The age you entered is invalid. Make sure the age is between 120-0.")

    else:

        statusMessage.configure(text="Creating account...", text_color="green")

        firstName = (realName.split(" ", 1))[0]
        uniqueUsername = f"{firstName[:3]}{userAge}"
        uniqueUsernameCreated = False
        index = 0

        while uniqueUsernameCreated is False:
            if uniqueUsername in userFile:
                uniqueUsername = f"{uniqueUsername}{index}"
                index += 1
            else:
                uniqueUsernameCreated = True

        userFile.update({uniqueUsername: { #Format used in order to save data
            "username": uniqueUsername,
            "password": inputPassword,
            "realName": realName,
            "age": userAge,
            "quizzesTaken": 0,
            "quizzes": {}
        }})

        saveUserData()
        mainMenu(root, uniqueUsername)

def main(root): #Login Screen

    clearScreen(root)

    mainTitle = customtkinter.CTkLabel(root, text="LOGIN/SIGNUP", font=("Arial", 30))
    mainTitle.pack(pady=20)

    logInButton = customtkinter.CTkButton(root, text="Log In", cursor="hand2", font=("Arial", 18), command=lambda: loginScreen(root))
    logInButton.pack(pady=40)

    signUpButton = customtkinter.CTkButton(root, text="Sign Up", cursor="hand2", font=("Arial", 18), command=lambda: signUpScreen(root))
    signUpButton.pack(pady=20)

    quitButton = customtkinter.CTkButton(root, text="Quit", command=root.destroy, cursor="hand2", font=("Arial", 18))
    quitButton.pack(pady=40)

    root.mainloop()

if __name__ == "__main__":

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk() #Creates the customtkinter window
    root.geometry("1440x900")
    root.title("OCRtunes")
    
    main(root)