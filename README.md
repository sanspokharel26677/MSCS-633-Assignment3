# MSCS-633-Assignment3: Terminal Q&A Chatbot using Django & ChatterBot

This project is a simple terminal-based Q&A chatbot built using **Python**, **Django**, and **ChatterBot**. The chatbot interacts with users in natural language, learns from conversations, and generates contextually relevant responses.

---

## 📁 Project Structure

```
MSCS-633-Assignment3/
├── chatbot_project/           # Django project folder
├── chat/                      # Django app containing chatbot logic
│   ├── chatbot.py             # Initializes and trains the chatbot
│   └── management/
│       └── commands/
│           └── chat.py        # Custom Django command to run chatbot via terminal
├── manage.py                  # Django entry point
├── README.md                  # Project overview and instructions
```

---

## 💬 Features

- Terminal-based chatbot interaction
- Built with ChatterBot NLP library
- Uses SQLite for storage and training data
- Learns from English corpus (ChatterBotCorpusTrainer)
- Handles conversation loop in terminal with `python manage.py chat`

---

## 🚀 How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/sanspokharel26677/MSCS-633-Assignment3.git
   cd MSCS-633-Assignment3
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python3.10 -m venv chatbot_env
   source chatbot_env/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install django
   pip install git+https://github.com/gunthercox/ChatterBot.git@master
   pip install chatterbot_corpus
   pip install pyyaml
   python -m spacy download en_core_web_sm
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Chat with the bot**
   ```bash
   python manage.py chat
   ```

---

## 🖼️ Screenshot

> 📸 **[Insert your screenshot here]**  
_Terminal output showing a conversation with the chatbot_

---

## 🧠 Sample Interaction

```
You: hello  
Bot: Hi  
You: how are you  
Bot: I am doing well.  
You: you are nice  
Bot: Thank you.  
You: exit  
Bot: Goodbye!
```

---

## 📦 Dependencies

- Python 3.10
- Django
- ChatterBot
- chatterbot_corpus
- spaCy (`en_core_web_sm`)
- PyYAML

---

## 🔧 Maintainer

**Sandesh Pokharel**  
MSCS Student, University of the Cumberlands

---

## 📝 License

This project is for academic use only.

