import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Supabase client
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("SUPABASE_URL or SUPABASE_KEY is not set in the .env file.")

supabase: Client = create_client(url, key)

# JSON data to insert into the quiz_questions table
'''
json_data = {
    "questionText": "Size of large data files can be reduced to save storage disk space. Which algorithm is appropriate to reduce size of large files?",
    "topic": "Data Compression",
    "difficultyLevel": "Medium",
    "choices": [
        {"choiceId": "a", "text": "Merge sort algorithm", "correct": False, "explanation": "Merge sort is used for sorting data, not for compression."},
        {"choiceId": "b", "text": "Huffman encoding algorithm", "correct": True, "explanation": "Huffman encoding is a lossless compression algorithm that reduces file size efficiently."},
        {"choiceId": "c", "text": "Heap sort algorithm", "correct": False, "explanation": "Heap sort is a sorting algorithm, not related to file compression."},
        {"choiceId": "d", "text": "Prim's algorithm", "correct": False, "explanation": "Prim's algorithm is used for finding minimum spanning trees in graphs, not for compression."}
    ],
    "correctAnswer": {"choiceId": "b", "reason": "Huffman encoding is the standard algorithm for reducing file size in lossless data compression."}
}

try:
    # Insert the JSON data into the table
    response = supabase.table('quiz_questions').insert({
        "question_text": json_data["questionText"],
        "topic": json_data["topic"],
        "difficulty_level": json_data["difficultyLevel"],
        "choices": json_data["choices"],
        "correct_answer": json_data["correctAnswer"]
    }).execute()


    print("Data inserted successfully:", response.data)
except Exception as e:
    print(f"Error inserting data: {e}")
'''

def create_document(question):
    try:
        response = supabase.table('quiz_questions').insert({
            "question_text": question['question_text'],
            "topic": question['topic'],
            "difficulty_level": question['difficulty_level'],
            "choices": question['choices'],
            "correct_answer": question['correct_answer']
        }).execute()
        print("Data inserted successfully:", response.data)
    except Exception as e:
        print(f"Error inserting data: {e}")
