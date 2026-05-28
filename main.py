#chat bot
print("Welcome to VIRU Chatbot")
print("You can ask me basic question,Type 'bye' to exit from the bot")
#response from chatbot
responses={
    "hi":"Hi, Welcome to our chatbot.\nHow can I help you",
    "how are you":"I am very fine. Thank you",
    "who are you":"I am smart AI chatbot",
    "help": "You can ask me about greetings, motivation, or basic questions.",
    "motivate me":"Keep grinding and Stay consistent you will shine one day"
    
    
}
#function
def getresponse(userque):
    userque=userque.lower().strip()

    
    for key in responses:
        if key in userque:
            return responses[key]
    return "Sorry,I am updating myself I don't know your answer"

# take inputs
while True:
    userinput=input("Ask you Question : ")
    
    if "bye" in userinput.lower():
        print("Thanks for reaching to us")
        break
    reply=getresponse(userinput)
    print("VIRU Response : ",reply)
