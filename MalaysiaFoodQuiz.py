#Importing necessary libraries
import streamlit as st
from PIL import Image

#Loading external question bank
questionBank = []

with open('question.txt', 'r') as txtfile:
    for line in txtfile:
        section = line.strip().split('::')
        #Question format
        currentQuestion = {
            "questionNo": section[0],
            "qAnswer": section[1],
            "question": section[2],
            "A": section[3],
            "B": section[4],
            "C": section[5],
            "D": section[6]
        }
        questionBank.append(currentQuestion)

#Creating sessions
if "currentPage" not in st.session_state:
    st.session_state.currentPage = "welcomePage"

if "username" not in st.session_state:
    st.session_state.username = ""

if "qAnswer" not in st.session_state:
    st.session_state.qAnswer = [None] * 4

#Title of WebApp
st.title("Malaysian Food Quiz")

#TODO ----- Welcome Page (Prompt for username input) -----
if st.session_state.currentPage == "welcomePage":

    st.divider()
    st.header("Welcome! Please enter your username before we begin:")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("Enter username:", value=st.session_state.username,
                                 placeholder= "Username")

        #Button to start quiz & check if user entered valid username
        if st.button("Press to Start"):
            if username.strip() == "":
                st.warning("Please enter a valid username before attempting.")
            else:
                st.session_state.username = username
                st.session_state.currentPage = "question1"
                st.rerun()
    st.divider()

#TODO ----- Type A: Question 1 -----
elif st.session_state.currentPage == "question1":
    currentQuestion = questionBank[0]

    #Display username and question number
    st.write("Username: ", st.session_state.username)
    st.subheader("Question No. 1")

    #Provide question and options
    ansChoice = st.radio(currentQuestion["question"], [currentQuestion["A"], currentQuestion["B"],
                                                 currentQuestion["C"], currentQuestion["D"]])
    st.session_state.qAnswer[0] = ansChoice

    #Button to move on to question 2
    col1, col2 = st.columns(2)
    with col2:
        if col2.button("Next"):
            st.session_state.currentPage = "question2"
            st.rerun()

#TODO ----- Type A: Question 2 -----
elif st.session_state.currentPage == "question2":
    currentQuestion = questionBank[1]

    #Display username and question number
    st.write("Username: ", st.session_state.username)
    st.subheader("Question No. 2")

    #Provide question and options
    ansChoice = st.radio(currentQuestion["question"], [currentQuestion["A"], currentQuestion["B"],
                                                 currentQuestion["C"], currentQuestion["D"]])
    st.session_state.qAnswer[1] = ansChoice

    #Back and Next button to move between questions
    col1, col2 = st.columns(2)
    #Back to previous question
    with col1:
        if col1.button("Back"):
            st.session_state.currentPage = "question1"
            st.rerun()

    #Next to question 3
    with col2:
        if col2.button("Next"):
            st.session_state.currentPage = "question3"
            st.rerun()

#TODO ----- Type B: Question 3 -----
elif st.session_state.currentPage == "question3":
    currentQuestion = questionBank[2]

    #Display username and question number
    st.write("Username: ", st.session_state.username)
    st.subheader("Question No. 3 ")

    #Opening image file & defining image width
    img = Image.open("nasilemak.jpg")
    st.image(img, width=400)

    #Provide question and options
    ansChoice = st.radio(currentQuestion["question"], [currentQuestion["A"], currentQuestion["B"],
                                                       currentQuestion["C"], currentQuestion["D"]])
    st.session_state.qAnswer[2] = ansChoice

    #Back and Next button to move between questions
    col1, col2 = st.columns(2)
    #Back to previous question
    with col1:
        if col1.button("Back"):
            st.session_state.currentPage = "question2"
            st.rerun()

    #Next to question 4
    with col2:
        if col2.button("Next"):
            st.session_state.currentPage = "question4"
            st.rerun()

#TODO ----- Type B: Question 4 -----
elif st.session_state.currentPage == "question4":
    currentQuestion = questionBank[3]

    # Display username and question number
    st.write("Username: ", st.session_state.username)
    st.subheader("Question No. 4")

    # Opening image file & defining image width
    img = Image.open("cendol.jpg")
    st.image(img, width=400)

    # Provide question and options
    ansChoice = st.radio(currentQuestion["question"], [currentQuestion["A"], currentQuestion["B"],
                                                 currentQuestion["C"], currentQuestion["D"]])
    st.session_state.qAnswer[3] = ansChoice

    #Back and Next button to move between questions
    col1, col2 = st.columns(2)
    #Back to previous question
    with col1:
        if col1.button("Back"):
            st.session_state.currentPage = "question3"
            st.rerun()

    #Next to question 4
    with col2:
        if col2.button("Submit"):
            st.session_state.currentPage = "finalResults"
            st.rerun()

#TODO ----- Displaying Results Page -----
elif st.session_state.currentPage == "finalResults":
    st.header("The Results are In!")
    totalScore = 0
    results = []

    #Marking correct answers with loop function
    for i in range(len(questionBank)):
        questions = questionBank[i]
        correct_answer = questions[questions["qAnswer"]]
        user_choice = st.session_state.qAnswer[i]

        #If user selects correct answer, +1 to totalScore
        if user_choice == correct_answer:
            totalScore += 1
            finalresut = "Correct Answer"

        else:
            finalresut = "Incorrect Answer"

        results.append({
            "Question:": questions["questionNo"],
            "User Selected:": user_choice,
            "Correct Answer:": correct_answer,
            "Results:": finalresut
        })

    #Output success message, user's total score with a summary of their results
    st.success(f"Congratulations {st.session_state.username}!")
    st.write(f"You have scored {totalScore} out of 4!")
    st.subheader("Summary Table")
    st.table(results)

    #Button to retry OR to end quiz
    col1, col2 = st.columns(2)
    #Button to retry
    with col1:
        if col1.button("Retry"):
            st.session_state.currentPage = "welcomePage"

    #Button to end quiz & save answer in external file
    with col2:
        if col2.button("Save & Quit"):
            with open("scores.txt", "a") as txtfile:
                txtfile.write("----------------------\n")
                txtfile.write(f"Username: {st.session_state.username}\n")

                for i in range(len(questionBank)):
                    txtfile.write(f"Question {i+1}: {st.session_state.qAnswer[i]}\n")

                txtfile.write(f"Final Score: {totalScore}\n")
                txtfile.write("----------------------\n")
                txtfile.write("\n")

            st.stop()

    st.divider()