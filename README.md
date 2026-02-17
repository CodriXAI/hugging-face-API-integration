# 🤖 Hugging Face API Integration – First AI Project

This is a simple AI-powered API that connects to a pre-trained model from [Hugging Face](https://huggingface.co) with the intention of understanding how to connect these models

---

## 🚀 Features

- Connects to a Hugging Face hosted model using an API token
- Accepts user input (text) and sends it to the model
- Returns answer in terminal
- Uses `.env` for secure token handling
- Built in Python 

---

## 🧠 What I Learned

- How to authenticate and consume a Hugging Face inference API
- How to manage API keys securely using environment variables
- How to build and test a basic AI service in Python
- How to structure and document a minimal backend project

---

## ⚙️ Tech Stack

- Python 3.x
- `requests` / `httpx` (API consumption)
- `python-dotenv` (env management)

---

## 📦 Installation & Setup

1. **Clone the repository**

   ```git
   git clone https://github.com/CodriXAI/hugging-face-API-integration.git
   cd hugging-face-API-integration
   ```

2. **Install dependencies**
    ```bash
    pip install -r requeriments.txt
    ```

3. **Create a `.env` file based on the provided example**
    ```bash
    cp .env.example .env
    ```

4. **Add your Hugging Face token to `.env`**
    ```.env
    HUGGINGFACE_TOKEN=your_token_here
    ```

5. **Run the app**
    ```bash
    python3 main.py
    ```
---

## 🔐 Security Notes
- Do **not share** your Hugging Face token publicly
- The `.env` file is excluded from git via `.gitignore`
- Make sure each user generates their own token from [Hugging Face Settings](https://huggingface.co/settings/tokens)

---

## 🧪 Example
Request:
```bash
python3 main.py
The Token has been loaded successfully
YOU: Hi chat!
```
Response:
```bash
python3 main.py
YOU: Hi chat!
BOT: It's nice to meet you. Is there something I can help you with, or would you like to chat?
```
**Note:** The actual output may vary depending on the model used.  
    
---

## 📜 License
This project is licensed under the MIT License. Feel free to use it as a base for your own ideas.

---

## Author
Built by **@Cristian "CodriX" Colares - AI beginner 🇦🇷**

---

