import aiml
import os

# Create an AIML Kernel
kernel = aiml.Kernel()

# Load AIML files
if os.path.exists("simple_chatbot.aiml"):
    kernel.learn("simple_chatbot.aiml")
else:
    print("Error: AIML file not found!")
    exit()

# Start the chat loop
print("ChatBot: Hello! Type 'quit' to exit.")
while True:
    user_input = input("You: ").strip().lower()  # Normalize input
    if user_input == "quit":
        print("ChatBot: Goodbye!")
        break
    response = kernel.respond(user_input)  # Get response from AIML
    if response:
        print(f"ChatBot: {response}")
    else:
        print("ChatBot: I don’t understand. Could you please rephrase?")
