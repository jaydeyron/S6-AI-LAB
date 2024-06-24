qa_pairs = {
    "Hi": "Hello",
    "What is your name?": "My name is ChatGPT.",
    "How are you?": "I'm doing well, thank you!",
    "What can you do?": "I can answer questions and have conversations with you.",
    "Goodbye": "Goodbye! Have a great day!"
}

def get_response(user):
    for question,value in qa_pairs.items():
        if question.lower()==user.lower():
            return value
    return "Sorry didn't catch that, try again"

while True:
    user=input("You: ")
    print("Chatbot: ",get_response(user))
    if(user.lower()=="goodbye"):
        exit()