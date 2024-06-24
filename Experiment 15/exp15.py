# simple chatbot

qa_pairs = {
    "Hi": "Hello",
    "What is your name?": "My name is ChatGPT.",
    "How are you?": "I'm doing well, thank you!",
    "What can you do?": "I can answer questions and have conversations with you.",
    "Goodbye": "Goodbye! Have a great day!"
}

def get_response(user_input):
    for question, answer in qa_pairs.items():
        if user_input.lower() == question.lower():
            return answer
    return "I'm sorry, I don't understand that. Could you kindly repeat yourself?"

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("ChatGPT:", response)
    if user_input.lower() == "goodbye":
        break