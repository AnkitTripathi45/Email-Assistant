# ✉️ Email Assistant

A powerful AI-powered email response generator that helps you craft professional, contextual, and tone-appropriate email responses using OpenAI's GPT model.

## 🌟 Features

- 📧 Auto-generate email responses based on email threads
- 🎭 Multiple tone options (Professional, Formal, Casual, Friendly)
- 📝 Smart subject line suggestions
- 📋 Email thread summarization
- 🎨 Modern and intuitive user interface
- 🔒 Secure API key management

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/email-assistant.git
cd email-assistant
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY="your-api-key-here"
```

### Running the Application

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## 💡 Usage

1. Enter your email thread in the input section
2. Select the desired tone for your response
3. Add any additional context or instructions
4. Click "Generate Response"
5. Review and copy the generated:
   - Subject line
   - Email response
   - Thread summary

## 🛠️ Project Structure

```
email-assistant/
├── app.py              # Main Streamlit application
├── utils.py           # Utility functions for OpenAI API calls
├── requirements.txt   # Project dependencies
├── .env              # Environment variables (API keys)
└── src/
    └── styles.css    # Custom CSS styles
```

## 🔧 Dependencies

- openai>=1.0.0
- python-dotenv>=1.0.0
- streamlit>=1.30.0

## 🔒 Security

- API keys are stored securely in environment variables
- No sensitive data is stored or transmitted
- All API calls are made securely to OpenAI's servers

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 🙏 Acknowledgments

- OpenAI for providing the GPT model
- Streamlit for the amazing web framework
- All contributors and users of this project

## 📞 Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.

---

Made with ❤️ by Ankit Tripathi