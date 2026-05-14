import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except:
    nltk.download('punkt', quiet=True)
try:
    nltk.data.find('corpora/stopwords')
except:
    nltk.download('stopwords', quiet=True)

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))
accounts = {"1234567890": 50000, "9876543210": 75000}

PATTERNS = {
    'greeting': r'\b(hello|hi|hey|greetings)\b',
    'balance': r'\b(balance|account|check)\b',
    'loan': r'\b(loan|borrow|credit|interest)\b',
    'contact': r'\b(contact|support|help|phone|email)\b',
    'bye': r'\b(bye|exit|quit|goodbye)\b'
}

RESPONSES = {
    'greeting': "Hi! I'm a bank chatbot. Choose 1-4 from menu.",
    'balance': "Choose option 1 to check balance.",
    'loan': "Loans available:\nHome: 7.5%\nEducation: 9%\nPersonal: 12%",
    'contact': "Call: 1800-123-456 or Email: support@bank.com",
    'bye': "Goodbye!"
}

def find_intent(text):
    for intent, pattern in PATTERNS.items():
        if re.search(pattern, text.lower()):
            return intent
    return None

def get_balance(acct):
    return f"Balance for {acct}: Rs. {accounts[acct]}" if acct in accounts else "Account not found"

def get_response(user_input):
    intent = find_intent(user_input)
    if intent is None:
        return "Choose a menu option (1-4) or type 'help'."
    return RESPONSES[intent]

MENU = "--- Bank Bot ---\n1. Balance\n2. Loans\n3. Support\n4. Exit\n"

def main():
    pending = False
    while True:
        try:
            print(MENU if not pending else "")
            user = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("Goodbye!")
            break
        
        if not user:
            continue
        
        if user == "1":
            print("Enter account (10 digits):")
            pending = "balance"
        elif user == "2":
            print("Bot:", RESPONSES['loan'])
        elif user == "3":
            print("Bot:", RESPONSES['contact'])
        elif user == "4":
            print("Bot: Goodbye!")
            break
        elif pending == "balance":
            if re.fullmatch(r"\d{10}", user):
                print("Bot:", get_balance(user))
                pending = False
            else:
                print("Invalid account number.")
        else:
            print("Bot:", get_response(user))
            if "goodbye" in get_response(user).lower():
                break

if __name__ == "__main__":
    main()