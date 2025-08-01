# Pet Name Generator

This is a simple web application built with Streamlit and LangChain that generates pet names based on user inputs.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/anandraja-dev/petname-generator.git
   cd petname-generator
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Set up your environment variables:**
   Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY="your-google-api-key"
   ```

4. **Run the application:**
   ```bash
   streamlit run main.py
   ```

## Dependencies

The application uses the following libraries:

- langchain-google-genai
- python-dotenv
- langchain-core
- streamlit
