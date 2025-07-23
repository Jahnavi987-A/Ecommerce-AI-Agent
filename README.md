🛍️ Ecommerce AI Agent

An intelligent AI-powered assistant that converts natural language questions into SQL queries and retrieves results from an e-commerce database.This project uses FastAPI for the backend, LLM (e.g., OpenAI via OpenRouter) to convert questions to SQL, and a clean HTML/CSS frontend for user interaction.

📌 Features

🧠 Converts natural language questions into SQL queries
🗃️ Executes SQL queries on an SQLite database
💬 Returns clean, readable query results
🌐 Simple and responsive frontend using HTML & CSS
🔒 Secure API key handling via .env

📁 Project Structure
        Ecommerce-AI-Agent/
        ├── api/
        │   └── main.py                # FastAPI application with endpoints
        ├── utils/
        │   ├── generate_sql.py       # Uses LLM to generate SQL from questions
        │   └── load_to_sql.py        # Executes SQL queries against the database
        ├── data/                     # Contains the SQLite database files
        │   └── ecommerce.db
        ├── frontend/                 # HTML frontend served by FastAPI
        │   └── index.html
        ├── .gitignore
        ├── requirements.txt
        ├── README.md
        └── .env                      # Contains

⚙️ Setup Instructions

1. Clone the Repository
   git clone https://github.com/Jahnavi987-A/Ecommerce-AI-Agent.git
   cd Ecommerce-AI-Agent
2. Create and Activate Virtual Environment (Optional but Recommended)
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
3. Install Requirements
   pip install -r requirements.txt
4. Add Your OpenAI API Key
   Create a .env file in the root folder and add:
   OPENAI_API_KEY=your_openai_key_here
   If you're using OpenRouter or another provider, update generate_sql.py accordingly.
5. Prepare Your Database
   Place your .db or .sqlite file inside the data/ folder. Ensure your tables and columns match the questions you'll ask.
6. Run the Server
   python -m uvicorn api.main:app --reload
   
Visit http://127.0.0.1:8000 in your browser to see the frontend.

🧪 Example Prompts
Ask any of these in the text area:

1."Which item had the highest total ad_sales?"
2."Show me the total sales by product ID."
3."What are the top 3 products sold this month?"
4."Give the average ad_sales for approved items."
5."Which category had the lowest sales yesterday?"

🛠️ Technologies Used

  Python 3.10+
  FastAPI
  OpenAI API / OpenRouter
  SQLite3
  HTML & CSS (Frontend)

💡 Future Improvements

  ✅ Add authentication
  📈 Graphical visualizations for query results
  📊 More flexible database support (PostgreSQL, MySQL)
  🤖 Use fine-tuned LLM for better SQL generation accuracy

🔗 License

  MIT License. See LICENSE file.

👤 Author

  Jahnavi Arthamuri
  GitHub Profile


   

