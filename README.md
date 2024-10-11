
# Thoughtful AI Customer Support Agent

This repository contains a simple customer support AI built using Streamlit and Google’s Gemini API to handle queries about Thoughtful AI. The AI answers user queries using predefined responses and can generate meaningful responses based on general knowledge when no predefined match is found.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites:
- Python 3.x
- `streamlit`
- `google.generativeai`
- `dotenv`
  
Install the required dependencies:
```bash
pip install -r requirements.txt
```

Ensure you have an API key for Google Gemini and add it to your `.env` file as GEMINI_API_KEY="key".

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/StarMindz/Thoughtful-Chat.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Thoughtful-Chat
   ```
3. Add your Google Gemini API key in the `.env` file:
   ```env
   GEMINI_API_KEY=your-api-key
   ```
4. Run the app:
   ```bash
   streamlit run main.py
   ```

## Features

- **Predefined Responses:** Uses predefined question-answer pairs for Thoughtful AI.
- **Fallback to General Knowledge:** If no match is found, the AI generates context-aware responses using Google Gemini.
- **Customizable Dataset:** Modify the `qa_pairs` for custom responses.
- **Interactive UI:** Built using Streamlit for user-friendly interaction.

## Contributing

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add new feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
