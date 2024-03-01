# FINAL PROJECT

# CHATBOT USING PYTHON AND NLP(Natural Language Processing)
# For making Chatbot i've used NLTK library, and imported Chat class
# from nltk.chat.util and reflections from nltk.chat.util.
# NLTK is one of the most widely used libraries for NLP in Python.

import nltk
from nltk.chat.util import Chat, reflections
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# this initializes NLTK resources
nltk.download('punkt')
nltk.download('vader_lexicon')

# In this code block, we define a list of patterns and
# responses that the chatbot will use to respond to user
# input.pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is PyBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"(.*) (good|great|well) ?",
        ["That's awesome to hear!",]
    ],
    [
        r"who created you?",
        ["I'm created by a group of three pyhton students",]
    ],
    [
        r"what are the names of them?",
        ["Muhammad Irtat Mobin, Syed Muhammad Yahya and Usman",]
    ],
    [
        r"what's the name of their Institute?",
        ["BANO QABIL 2.0",]
    ],
    [
        r"what is the name of their Instructor?",
        ["Fahad Bin Ashfaq",]
    ],
    [
        r"What is Python?",
        ["Python is a high-level programming language known for its simplicity, readability, and versatility.",]
    ],
    [
        r"What is Variable?",
        ["A variable in Python is a named storage location used to store data that can be referenced and manipulated within a program.",]
    ],
    [
        r"How many data types are there in python?",
        ["Python includes several built-in data types such as integers, floats, complex numbers, strings, lists, tuples, dictionaries, sets, and booleans.",]
    ],
    [
        r"How many loops are used python?",
        ["In Python, there are two main types of loops: the for loop and the while loop. Additionally, Python supports loop control statements such as break and continue to modify loop behavior.",]
    ],
    [
        r"How many things can we do using python?",
        ["The possibilities with Python are virtually limitless. Some common applications of Python include web development, data analysis, machine learning, artificial intelligence, automation, scripting, game development, scientific computing, and more. Python's extensive standard library and vast ecosystem of third-party packages enable developers to tackle a wide range of tasks efficiently and effectively.",]
    ],
    [
        r"Who invented python?",
        ["Python was created by Guido van Rossum, a Dutch programmer, in the late 1980s.",]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help you with that. What do you need assistance with?",]
    ],
    [
        r"(.*) (quit|bye|exit) ?",
        ["Goodbye! Have a great day.",]
    ],
]

# We've Created a chatbot using the defined pairs and reflections
chatbot = Chat(pairs, reflections)
sid = SentimentIntensityAnalyzer()

# We've created a chat function
def chat():
    print("Hi! I'm PyBot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        # Perform sentiment analysis on user input
        sentiment_score = sid.polarity_scores(user_input)
        if sentiment_score['compound'] >= 0.5:
            print("You seem positive!")
        elif sentiment_score['compound'] <= -0.5:
            print("You seem negative. Is everything okay?")
        else:
            print("Your sentiment is neutral.")
        # Get response from chatbot
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() in ["quit", "bye", "exit"]:
            break

# We've used this method of Call the chat function to start interacting with the ChatBot
if __name__ == "__main__":
    chat()