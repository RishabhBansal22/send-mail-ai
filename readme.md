# 📧 send-mail-ai

A simple, intelligent Python tool that lets you send emails using natural language — powered by Google Gemini AI!  
No more manually writing email subjects, content, or even choosing attachments. Just tell the AI what you want, and it takes care of the rest.

---

## ✨ Features

- **Smart Email Generation:**  
  Simply describe your intent (e.g., "Send a thank-you email to Alice"), and the AI will craft the subject and body for you.
- **Automated Personalization:**  
  The AI extracts names from email addresses and uses them to personalize your message.
- **Attachment Support:**  
  Ask the AI to include files as attachments — just reference the document, and it’s added automatically.
- **Easy to Use CLI:**  
  Interact with the assistant right from your terminal.

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/RishabhBansal22/send-mail-ai.git
cd send-mail-ai
```

### 2. Install dependencies

> **Note:** Requires Python 3.8+

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```env
gmail_app_pass=your_gmail_app_password
gemini_api_key=your_gemini_api_key
```

- `gmail_app_pass`: [Generate a Gmail App Password](https://support.google.com/accounts/answer/185833)
- `gemini_api_key`: Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 4. Run the assistant

```bash
python main.py
```

And type your email request in natural language!

---

## 🧩 Example Usages

```txt
USER : Send an email to alice@example.com from bob@example.com
```

AI will generate:
- Subject: Hello Alice from Bob
- Body: Hi Alice, This is Bob. I hope you are well.

---

```txt
USER : Email john@company.com with the report attached
```

AI will infer:
- Subject: Report for John
- Body: Hi John, Please find the attached report.
- Attachment: (asks for file path)

---

## ⚙️ How It Works

- Uses [Google Gemini AI](https://deepmind.google/technologies/gemini/) to understand your intent and generate email content.
- Modular design with:
  - `GeminiAssistant`: Handles AI interaction & email intent parsing.
  - `SendMail`: Builds and sends emails (with or without attachments).
- Sends email securely via Gmail SMTP.

---

## 📂 Project Structure

```
send-mail-ai/
│
├── main.py                # CLI entrypoint
├── src/
│   ├── gemini.py          # GeminiAssistant class & AI logic
│   └── send_mail.py       # SendMail class for sending emails
├── prompts/
│   └── system.py          # System instructions and AI prompt templates
├── requirements.txt
└── .env.example           # Example environment config
```

---

## 🙏 Acknowledgements

- Powered by [Google Gemini](https://deepmind.google/technologies/gemini/)
- Inspired by the need for fast, smart, and personalized email automation.

---

## 📝 License

This project is open-source. See the [LICENSE](LICENSE) file for more details.

---

## ✉️ Contribute

Pull requests and suggestions are welcome!  
Let’s make email easier for everyone.

---