#TODO ----- Statistical Insights Page -----
#Importing necessary libraries
import streamlit as st
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Title of WebApp
st.title("Statistical Insights from Malaysia Food Quiz ")

#Storing elements into lists
participantName = []
question1 = []
question2 = []
question3 = []
question4 = []
participantTScores = []

#Reading & Appending scores.txt file
with open("scores.txt", "r") as txtfile:
    for line in txtfile:
        if "Username:" in line:
            username = line.split(":")[1].strip()
            participantName.append(username)

        elif "Question 1:" in line:
            q1 = line.split(":")[1].strip()[0]
            question1.append(q1)

        elif "Question 2:" in line:
            q2 = line.split(":")[1].strip()[0]
            question2.append(q2)

        elif "Question 3:" in line:
            q3 = line.split(":")[1].strip()[0]
            question3.append(q3)

        elif "Question 4:" in line:
            q4 = line.split(":")[1].strip()[0]
            question4.append(q4)

        elif "Final Score:" in line:
            fScore = int(line.split(":")[1].strip())
            participantTScores.append(fScore)

#TODO ----- Display Summary table for all participant scores -----
#Subheader
st.divider()
st.subheader("Summary Table")

#Establish Correct Answers from question.txt file
qAnswer = []

#For loop for automation instead of hardcoding correct question answers
with open("question.txt", "r") as txtfile:
    for line in txtfile:
        section = line.strip().split('::')
        qAnswer.append(section[1])

#Create list to store elements
participantQ1 = []
participantQ2 = []
participantQ3 = []
participantQ4 = []

#Run for loop for Summary Table
for i in range(len(participantName)):
    if question1[i] == qAnswer[0]:
        participantQ1.append("Correct")
    else:
        participantQ1.append("Incorrect")

    if question2[i] == qAnswer[1]:
        participantQ2.append("Correct")
    else:
        participantQ2.append("Incorrect")

    if question3[i] == qAnswer[2]:
        participantQ3.append("Correct")
    else:
        participantQ3.append("Incorrect")

    if question4[i] == qAnswer[3]:
        participantQ4.append("Correct")
    else:
        participantQ4.append("Incorrect")

#Dataframe Creation for Summary Table
summaryTable = pd.DataFrame({"Username": participantName,
                             "Question 1": participantQ1,
                             "Question 2": participantQ2,
                             "Question 3": participantQ3,
                             "Question 4": participantQ4,
                             "Final Score": participantTScores
                             })

#Displaying Summary Table
st.table(summaryTable)
st.divider()

#TODO ----- Matrix of Quiz Results by all Participants -----
#Subheader
st.subheader("Quiz Matrix Results")

#Creating new columns (Percentage % & No. of Questions)
percentageScore = []

#For loop for automation instead of hardcoding no. of questions
totalQNo = 0
with open("question.txt", "r") as txtfile:
    for line in txtfile:
        totalQNo += 1

#Calculating %
for fScore in participantTScores:
    participantPercentage = f"{(fScore / totalQNo) * 100: .2f}"
    percentageScore.append(participantPercentage)

#Dataframe Creation for Quiz Matrix
quizMatrix = pd.DataFrame({"Username": participantName,
                           "Question 1": question1,
                           "Question 2": question2,
                           "Question 3": question3,
                           "Question 4": question4,
                           "Final Score": participantTScores,
                           "Percentage Score(%)": percentageScore
                           })

#DIsplay Quiz Matrix Results
st.table(quizMatrix)
st.divider()

#TODO ----- Quiz Statistics (Max, Min, Mean, Median & Average) -----
#Subheader
st.subheader("Total Quiz Statistics")

#Calculating statistics
highestPscore = max(participantTScores)
lowestPscore = min(participantTScores)
averagePscore = sum(participantTScores) / len(participantTScores)
medianPscore = statistics.median(participantTScores)
meanPscore = statistics.mean(participantTScores)

#Display statistics in columns
col1, col2 = st.columns(2)
with col1:
    st.write(f"Highest Participant Score: {highestPscore: .2f}")
    st.write(f"Lowest Participant Score: {lowestPscore: .2f}")
    st.write(f"Average Participant Score: {averagePscore: .2f}")

with col2:
    st.write(f"Median Participant Score: {medianPscore: .2f}")
    st.write(f"Mean Participant Score: {meanPscore: .2f}")

st.divider()

#TODO -----Statistical Graphs (Total Marks, Average, Median, Mean) -----
#Subheader
st.subheader("Statistical Graphs")

#Displaying bar graphs in columns
col1, col2 = st.columns(2)
with col1:
    st.write("Graph for Total Marks")
    fig, ax = plt.subplots()
    ax.bar(participantName, participantTScores, color = "green")
    ax.title.set_text("Total Marks per Participant")
    ax.set_xlabel("Participant")
    ax.set_ylabel("Marks Obtained")
    ax.set_yticks(np.arange(0.0, 4.1, 0.5))

    #Displaying on Streamlit
    st.pyplot(fig)

    st.write("Graph for Median")
    fig, ax = plt.subplots()
    ax.bar(participantName, medianPscore, color = "blue")
    ax.title.set_text("Median of Participants Score")
    ax.set_xlabel("Participant")
    ax.set_ylabel("Median")
    ax.set_yticks(np.arange(0.0, 4.1, 0.5))

    #Displaying on Streamlit
    st.pyplot(fig)

with col2:
    st.write("Graph for Average")
    fig, ax = plt.subplots()
    ax.bar(participantName, averagePscore, color = "purple")
    ax.title.set_text("Average of Participants Score")
    ax.set_xlabel("Participant")
    ax.set_ylabel("Average")
    ax.set_yticks(np.arange(0.0, 4.1, 0.5))

    #Displaying on Streamlit
    st.pyplot(fig)

    st.write("Graph for Mean")
    fig, ax = plt.subplots()
    ax.bar(participantName, meanPscore, color = "red")
    ax.title.set_text("Mean of Participants Score")
    ax.set_xlabel("Participant")
    ax.set_ylabel("Mean")
    ax.set_yticks(np.arange(0.0, 4.1, 0.5))

    #Displaying on Streamlit
    st.pyplot(fig)

#Button to leave Statistics Page
col1, col2, col3 = st.columns(3)
with col2:
    if col2.button("Leave"):
        st.stop()