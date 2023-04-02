import sqlite3
import requests

TEXTCORTEX_API_KEY = 'Bearer YOUR_API_KEY'
TEXTCORTEX_SQL_GENERATOR_API_ENDPOINT = "https://api.textcortex.com/v1/codes"
# This is the database we want to query
DATABASE = 'bike_store.db'
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()


def fetch_all_table_structure():
    """
    This function fetches all of the tables structure of the database and returns as a dictionary
    :return:
    """
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_structure = {}
    for table in tables:
        cursor.execute(f"PRAGMA table_info({table[0]})")
        table_structure[table[0]] = cursor.fetchall()
    return table_structure


# We can fetch the table structure once and use it for all the questions
table_structure = fetch_all_table_structure()


def generate_sql_query(question, table_structure):
    """
    This function generates the SQL query by making a POST request to TextCortex API with
     the user question and the table structure
    :param question: user question
    :param table_structure: table structure of the database
    :return: SQL query
    """
    payload = {
        "max_tokens": 1024,
        "mode": "python",
        "model": "icortex-1",
        "n": 1,
        "temperature": 0,
        "text": "SQL Table Structure: " + str(table_structure) + " Question: " + question + " SQL Query: "
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": TEXTCORTEX_API_KEY
    }
    response = requests.request("POST", TEXTCORTEX_SQL_GENERATOR_API_ENDPOINT, json=payload, headers=headers)
    if response.status_code == 200:
        # Execute SQL query and display results
        sql_query = response.json()['data']['outputs'][0]['text']
        print(f"Generated SQL query: {sql_query}")
        cursor.execute(sql_query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    else:
        print("Ups, that didn't work. Can you rephrase your question?", response.text)
    # Close connection
    return response


if __name__ == '__main__':
    # Ask user for question
    while question := input(f"What would you like to ask to {DATABASE} database? "):
        generate_sql_query(question, table_structure)
