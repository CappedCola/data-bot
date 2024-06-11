import openai
import sqlite3
import os


#modified with git 
#pushed to main branch
openai_api_key = os.getenv("OPENAI_API_KEY")

conn = sqlite3.connect('codexPromptData.db')
curr = conn.cursor()
prompt = 'Can you turn this set of instructions for an AI into 5 questions that can be understood for an AI. Reword the questions making them sound human like and add in some extra detail to the instructions. Make the questions not wordy. Make the instructions declarative. Give me the questions in a list format with dashes in front of each question. The instructions are, "'
query = "SELECT * FROM Prompts"




def ask_chatgpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature = 1.25,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            max_tokens=100  # Reduce the number of tokens to stay within quota
        )
        answer = response.choices[0]['message']['content'].strip()
        return answer
    except Exception as e:
        return f"An error occurred: {e}"

# Execute the query to fetch the row with id=1
curr.execute(query)
rows = curr.fetchall()
numRows = len(rows)

# Check if the row is found
'''
if rows:
    row_string = ', '.join(str(value) for value in rows[1:])
    # Concatenate the prompt with the fetched row data
    GPTPrompt = prompt + row_string + '"'
    # Get the ChatGPT response
    response = ask_chatgpt(GPTPrompt)
    print(response)
else:
    print("Row not found")

'''
# Close the cursor and the connection
curr.close()
conn.close()
