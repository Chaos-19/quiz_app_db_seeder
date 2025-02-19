import os
import json
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from dotenv import load_dotenv
from appwrite.query import Query


from supabase_script import create_document

# Load environment variables from .env file
load_dotenv()
# Initialize the Appwrite client
client = Client()
client.set_endpoint(os.getenv('APPWRITE_ENDPOINT'))  # Ensure this is the correct endpoint
client.set_project(os.getenv('PROJECT_ID'))
client.set_key(os.getenv('API_KEY'))

# Initialize the Databases service
databases = Databases(client)

'''
def prepare_database():
    try:
        # Create a database
        questionDatabase = databases.create(
            database_id=ID.unique(),
            name='QuestionsDB'
        )
        print("Database created successfully:", questionDatabase)

        # Create a collection
        questionCollection = databases.create_collection(
            database_id=questionDatabase['$id'],
            collection_id=ID.unique(),
            name='Questions',
            permissions=[]
        )
        print("Collection created successfully:", questionCollection)

        # Add attributes to the collection
        databases.create_string_attribute(
            database_id=questionDatabase['$id'],
            collection_id=questionCollection['$id'],
            key='questionText',
            size=500,  # Adjust size as needed
            required=True
        )
        databases.create_string_attribute(
            database_id=questionDatabase['$id'],
            collection_id=questionCollection['$id'],
            key='topic',
            size=255,
            required=True
        )
        databases.create_string_attribute(
            database_id=questionDatabase['$id'],
            collection_id=questionCollection['$id'],
            key='difficultyLevel',
            size=50,
            required=True
        )
        databases.create_string_attribute(
            database_id=questionDatabase['$id'],
            collection_id=questionCollection['$id'],
            key='choices',
            size=8192,  # Adjust size as needed
            required=True
        )
        databases.create_string_attribute(
            database_id=questionDatabase['$id'],
            collection_id=questionCollection['$id'],
            key='correctAnswer',
            size=1024,
            required=True
        )
        return questionDatabase, questionCollection
    except Exception as e:
        print("Failed to prepare database:", e)

def seed_database(questionDatabase, questionCollection):
    question1 = {
        'questionText': "Consider the following fragment of C++ code:\n\nconst int x = 8;\nconst int y = 16;\nif(x > y)\n{\n int z = x + y;\n}\n\nFor codes like the above one, which technique of code optimization is appropriate?",
        'topic': "Code Optimization",
        'difficultyLevel': "Medium",
        'choices': [
            {
                'choiceId': 'a',
                'text': "Arithmetic simplification",
                'correct': False,
                'explanation': "Arithmetic simplification involves simplifying arithmetic expressions, but this code doesn't have complex expressions that can be simplified."
            },
            {
                'choiceId': 'b',
                'text': "Compile time evaluation",
                'correct': False,
                'explanation': "Compile-time evaluation can be applied to compute const expressions. However, the if statement's condition will still evaluate at runtime, and 'z' will not be computed."
            },
            {
                'choiceId': 'c',
                'text': "Code motion",
                'correct': False,
                'explanation': "Code motion moves loop invariant code outside of a loop, which isn't applicable to this snippet."
            },
            {
                'choiceId': 'd',
                'text': "Dead code elimination",
                'correct': True,
                'explanation': "Dead code elimination removes code that does not affect the program's outcome, which is applicable here as 'z' is never used."
            }
        ],
        'correctAnswer': {
            'choiceId': 'd',
            'reason': "Dead code elimination removes code that does not affect the program's outcome, which is applicable here as 'z' is never used."
        }
    }

    try:
        databases.create_document(
            database_id=questionDatabase['$id'],
            collection_id=questionCollection['$id'],
            document_id=ID.unique(),
            data={
                'questionText': question1['questionText'],
                'topic': question1['topic'],
                'difficultyLevel': question1['difficultyLevel'],
                'choices': json.dumps(question1['choices']),  # Convert choices to JSON string
                'correctAnswer': json.dumps(question1['correctAnswer'])  # Convert correctAnswer to JSON string
            }
        )
        print("Document created successfully.")
    except Exception as e:
        print("Failed to create document:", e)

if __name__ == "__main__":
    questionDatabase, questionCollection = prepare_database()
    if questionDatabase and questionCollection:
        seed_database(questionDatabase, questionCollection)
        
        
        


def create_document(question):
    try:
        databases.create_document(
            database_id=os.getenv('DATABASE_ID'),
            collection_id=os.getenv('COLLECTION_ID'),
            document_id=ID.unique(),
            data={
                'questionText': question['question']['questionText'],
                'topic': question['question']['topic'],
                'difficultyLevel': question['question']['difficultyLevel'],
                'choices': json.dumps(question['question']['choices']),  
                'correctAnswer': json.dumps(question['question']['correctAnswer']) 
            }
        )
        print("Document created successfully.")
    except Exception as e:
        print("Failed to create document:", e)
        
'''   
        
        
'''open("output.json", "w").write(json.dumps(databases.list_documents(
    database_id=os.getenv('DATABASE_ID'),
    collection_id=os.getenv('COLLECTION_ID')
)))

print("Documents listed successfully.")
'''

result = databases.list_documents(
    database_id=os.getenv('DATABASE_ID'),
    collection_id=os.getenv('COLLECTION_ID'),
    queries=[
            Query.limit(100),
            Query.offset(100),
        ]
) 
  
print(len(result['documents']))
for document in result['documents']:
     document['choices'] = json.loads(document['choices'])
     document['correctAnswer'] = json.loads(document['correctAnswer'])
     
     create_document( {
            "question_text": document['questionText'],
            "topic": document['topic'],
            "difficulty_level": document['difficultyLevel'],
            "choices": document['choices'],
            "correct_answer": document['correctAnswer']
        })
     '''
     print("Document created successfully.")'''