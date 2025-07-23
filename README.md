# 🛍️ Ecommerce AI Agent

An intelligent AI-powered assistant that converts natural language questions into SQL queries and retrieves results from an e-commerce database.This project uses FastAPI for the backend, LLM (e.g., OpenAI via OpenRouter) to convert questions to SQL, and a clean HTML/CSS frontend for user interaction.

## 📌 Features

🧠 Converts natural language questions into SQL queries <br>
🗃️ Executes SQL queries on an SQLite database <br>
💬 Returns clean, readable query results <br>
🌐 Simple and responsive frontend using HTML & CSS <br>
🔒 Secure API key handling via .env <br>

## 📁 Project Structure<br>
Ecommerce-AI-Agent/<br>
├── api/<br>
│ └── main.py # FastAPI application with endpoints<br>
├── utils/<br>
│ ├── generate_sql.py # Uses LLM to generate SQL from questions<br>
│ └── load_to_sql.py # Executes SQL queries against the database<br>
├── data/ # Contains the SQLite database files<br>
│ └── ecommerce.db<br>
├── frontend/ # HTML frontend served by FastAPI<br>
│ └── index.html<br>
├── .gitignore<br>
├── requirements.txt<br>
├── README.md<br>
└── .env # Contains your OpenAI API key (excluded from Git)<br>

## ⚙️ Setup Instructions

1. Clone the Repository<br>
   git clone https://github.com/Jahnavi987-A/Ecommerce-AI-Agent.git<br>
   cd Ecommerce-AI-Agent<br>
   
2. Create and Activate Virtual Environment (Optional but Recommended)<br>
   python -m venv venv<br>
   venv\Scripts\activate  - Windows<br>
   source venv/bin/activate  - macOS/Linux<br>
3. Install Requirements<br>
   pip install -r requirements.txt<br>
4. Add Your OpenAI API Key<br>
   Create a .env file in the root folder and add:<br>
   OPENAI_API_KEY=your_openai_key_here<br>
   If you're using OpenRouter or another provider, update generate_sql.py accordingly.<br>
5. Prepare Your Database<br>
   Place your .db or .sqlite file inside the data/ folder. Ensure your tables and columns match the questions you'll ask.<br>
6. Run the Server<br>
   python -m uvicorn api.main:app --reload<br>
   
### **Visit http://127.0.0.1:8000 in your browser to see the frontend.**<br>


## 🧪 Example Prompts
Ask any of these in the text area:

1."Which item had the highest total ad_sales?"<br>
2."Show me the total sales by product ID."<br>
3."What are the top 3 products sold this month?"<br>
4."Give the average ad_sales for approved items."<br>
5."Which category had the lowest sales yesterday?"<br>

## 🛠️ Technologies Used

  Python 3.10+<br>
  FastAPI<br>
  OpenAI API / OpenRouter<br>
  SQLite3<br>
  HTML & CSS (Frontend)<br>

## 💡 Future Improvements

  ✅ Add authentication <br>
  📈 Graphical visualizations for query results <br>
  📊 More flexible database support (PostgreSQL, MySQL) <br>
  🤖 Use fine-tuned LLM for better SQL generation accuracy <br>


## 🔗 License

  MIT License. See LICENSE file.



## 👤 Author

  Jahnavi Arthamuri
  GitHub Profile


   

