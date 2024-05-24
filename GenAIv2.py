# Project:  GenAI
# Author:  Sarah Pfeiffer

# Focus:  Implement rule-based logic for a financial chatbot
# Chatbot sample dialogue


# Selection of 5 predefined questions

# function to take the user input and map it to the correct answer.
def user_query(response):
    if response.lower() == "what is net income?":
        print("Bot: Net income is 72,361")
    elif response.lower() == "what is the debt ratio?":
        print("Bot: The debt ratio is .5. 50% of assets are owned by creditors.")
    elif response.lower() == "how has total revenue changed?":
        print("Bot: Total revenue increased 6.88%")
    elif response.lower() == "what was total liabilities in 2022?":
        print("Bot: Total liabilities was 198,298 in 2022")
    elif response.lower() == "how has cash flow from operations changed?":
        print("Bot: Cash flow from operating activities decreased 1.63%")
    else:
        print("Bot: Sorry, I can only provide information on predefined queries.\n Ask about net income, debt ratio, total liabilities or cash flow from operations. ")

# main function to excute the script
def main():
    print("Welcome to the financial chatbot.  This chatbot can only respond to predefined questions.")
    print("Sample formats for questions:  What is [financial measure]? or How has [financial measure] changed?")
    print("")
    print("Bot:  What is your question? Enter q to quit.")
   
    while True:
        response = input("You: ")
        if response.lower() == "q":
            print("Bot: Bye")
            break
        user_query(response.lower())

main()



    

    
    
    
    
