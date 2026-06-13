import datetime
import random

# -----------------------------
# CHATBOT DATA
# -----------------------------

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why do Java developers wear glasses? Because they can't C!",
    "Why was Python sad? Because it had too many exceptions."
]

facts = [
    "The first computer bug was an actual bug.",
    "Python was created by Guido van Rossum in 1991.",
    "Artificial Intelligence is transforming every industry."
]

positive_words = ["happy", "good", "great", "awesome", "excellent"]
negative_words = ["sad", "bad", "upset", "angry", "tired"]

conversation_history = []

# -----------------------------
# FUNCTIONS
# -----------------------------

def save_chat(user_msg, bot_msg):
    conversation_history.append(
        {
            "user": user_msg,
            "bot": bot_msg
        }
    )

def display_history():
    print("\n------ CHAT HISTORY ------")

    if not conversation_history:
        print("No conversation yet.")

    for chat in conversation_history:
        print(f"You : {chat['user']}")
        print(f"Bot : {chat['bot']}")
        print()

def detect_mood(text):
    text = text.lower()

    for word in positive_words:
        if word in text:
            return "positive"

    for word in negative_words:
        if word in text:
            return "negative"

    return "neutral"

def calculator():
    print("\n===== CALCULATOR =====")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+,-,*,/): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result =", num1 + num2)

        elif op == "-":
            print("Result =", num1 - num2)

        elif op == "*":
            print("Result =", num1 * num2)

        elif op == "/":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print("Result =", num1 / num2)

        else:
            print("Invalid operator")

    except ValueError:
        print("Invalid Input")

def show_help():
    print("""
========= COMMANDS =========

hello / hi
how are you
time
date
calculator
joke
fact
history
help
bye

============================
""")

# -----------------------------
# MAIN PROGRAM
# -----------------------------

print("=" * 60)
print("      DECODELABS RULE-BASED AI CHATBOT")
print("=" * 60)

name = input("Enter your name: ").title()

print(f"\nWelcome {name}!")
print("I am your Rule-Based AI Assistant.")
print("Type 'help' to see commands.\n")

interaction_count = 0

while True:

    user_input = input(f"{name}: ").strip().lower()

    interaction_count += 1

    # Greetings
    if user_input in ["hi", "hello", "hey"]:

        responses = [
            f"Hello {name}!",
            f"Nice to see you {name}.",
            f"Hey {name}, how can I help?"
        ]

        bot_response = random.choice(responses)

    elif "how are you" in user_input:

        bot_response = random.choice([
            "I'm doing great!",
            "Working perfectly!",
            "Ready to help you."
        ])

    elif user_input == "time":

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        bot_response = f"Current Time: {current_time}"

    elif user_input == "date":

        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        bot_response = f"Today's Date: {current_date}"

    elif user_input == "joke":

        bot_response = random.choice(jokes)

    elif user_input == "fact":

        bot_response = random.choice(facts)

    elif user_input == "calculator":

        calculator()
        continue

    elif user_input == "history":

        display_history()
        continue

    elif user_input == "help":

        show_help()
        continue

    elif user_input in ["bye", "exit", "quit"]:

        print("\n========== SESSION SUMMARY ==========")
        print("User Name :", name)
        print("Interactions :", interaction_count)
        print("Conversation Saved :", len(conversation_history))
        print("=====================================")

        print(f"\nBot: Goodbye {name}! Have a wonderful day.")
        break

    else:

        mood = detect_mood(user_input)

        if mood == "positive":
            bot_response = "That's wonderful to hear! Keep smiling."

        elif mood == "negative":
            bot_response = "I hope things get better soon. Stay positive."

        else:
            bot_response = (
                "Sorry, I don't understand that. "
                "Type 'help' to see available commands."
            )

    print("Bot:", bot_response)

    save_chat(user_input, bot_response)
