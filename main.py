import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()



genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
    upload_to_gemini("./image-one.png", mime_type="image/png"),
    upload_to_gemini("./image.png", mime_type="image/png"),
]



history=[
    {
      "role": "user",
      "parts": [
        files[0],
        "You are given an image containing a multiple-choice question. Your task is to extract the data from the image and format it into a structured JSON format like the one below '{\n  \"question\": {\n    \"id\": 2,\n    \"questionText\": \"Size of large data files can be reduced to save storage disk space. Which algorithm is appropriate to reduce size of large files?\",\n    \"topic\": \"Data Compression\",\n    \"difficultyLevel\": \"Medium\",\n    \"estimatedTime\": \"1 minute\",\n    \"choices\": [\n      {\n        \"choiceId\": \"a\",\n        \"text\": \"Merge sort algorithm\",\n        \"correct\": false,\n        \"explanation\": \"Merge sort is used for sorting data, not for compression.\"\n      },\n      {\n        \"choiceId\": \"b\",\n        \"text\": \"Huffman encoding algorithm\",\n        \"correct\": true,\n        \"explanation\": \"Huffman encoding is a lossless compression algorithm that reduces file size efficiently.\"\n      },\n      {\n        \"choiceId\": \"c\",\n        \"text\": \"Heap sort algorithm\",\n        \"correct\": false,\n        \"explanation\": \"Heap sort is a sorting algorithm, not related to file compression.\"\n      },\n      {\n        \"choiceId\": \"d\",\n        \"text\": \"Prim's algorithm\",\n        \"correct\": false,\n        \"explanation\": \"Prim's algorithm is used for finding minimum spanning trees in graphs, not for compression.\"\n      }\n    ],\n    \"correctAnswer\": {\n      \"choiceId\": \"b\",\n      \"reason\": \"Huffman encoding is the standard algorithm for reducing file size in lossless data compression.\"\n    }\n  }\n}\n'",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"question\": {\n    \"id\": 2,\n    \"questionText\": \"Size of large data files can be reduced to save storage disk space. Which algorithm is appropriate to reduce size of large files?\",\n    \"topic\": \"Data Compression\",\n    \"difficultyLevel\": \"Medium\",\n    \"estimatedTime\": \"1 minute\",\n    \"choices\": [\n      {\n        \"choiceId\": \"a\",\n        \"text\": \"Merge sort algorithm\",\n        \"correct\": false,\n        \"explanation\": \"Merge sort is used for sorting data, not for compression.\"\n      },\n      {\n        \"choiceId\": \"b\",\n        \"text\": \"Huffman encoding algorithm\",\n        \"correct\": true,\n        \"explanation\": \"Huffman encoding is a lossless compression algorithm that reduces file size efficiently.\"\n      },\n      {\n        \"choiceId\": \"c\",\n        \"text\": \"Heap sort algorithm\",\n        \"correct\": false,\n        \"explanation\": \"Heap sort is a sorting algorithm, not related to file compression.\"\n      },\n      {\n        \"choiceId\": \"d\",\n        \"text\": \"Prim's algorithm\",\n         \"correct\": false,\n        \"explanation\": \"Prim's algorithm is used for finding minimum spanning trees in graphs, not for compression.\"\n      }\n    ],\n    \"correctAnswer\": {\n      \"choiceId\": \"b\",\n      \"reason\": \"Huffman encoding is the standard algorithm for reducing file size in lossless data compression.\"\n    }\n  }\n}\n```\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[1],
        "get the json for this\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"question\": {\n    \"id\": 3,\n    \"questionText\": \"Which one of the following is asynchronous in message communication?\",\n    \"topic\": \"Message Passing\",\n    \"difficultyLevel\": \"Medium\",\n    \"estimatedTime\": \"1 minute\",\n    \"choices\": [\n      {\n        \"choiceId\": \"a\",\n        \"text\": \"Blocking send\",\n        \"correct\": false,\n        \"explanation\": \"Blocking send operation waits until the message is received, making it synchronous.\"\n      },\n      {\n        \"choiceId\": \"b\",\n        \"text\": \"Blocking receive\",\n        \"correct\": false,\n        \"explanation\": \"Blocking receive waits until a message is available, making it synchronous.\"\n      },\n      {\n        \"choiceId\": \"c\",\n         \"text\": \"Direct message\",\n        \"correct\": false,\n        \"explanation\": \"Direct messaging can be either synchronous or asynchronous depending on the implementation of send/receive operations, not inherently asynchronous.\"\n      },\n      {\n        \"choiceId\": \"d\",\n        \"text\": \"Non-block receive\",\n        \"correct\": true,\n        \"explanation\": \"Non-blocking receive checks for a message and returns immediately regardless of whether a message is available, making it asynchronous.\"\n      }\n    ],\n    \"correctAnswer\": {\n      \"choiceId\": \"d\",\n       \"reason\": \"Non-blocking receive operations allow a process to continue executing without waiting for a message, thus achieving asynchronous communication.\"\n    }\n  }\n}\n```\n",
      ],
    },
  ]

def get_json_from_image(image_path):
    uploaded_file = upload_to_gemini(image_path, mime_type="image/jpeg")

    
    chat_session = model.start_chat(history=[{
                "role": "user",
                "parts": [
                    uploaded_file,
                    "You are given an image containing a multiple-choice question. Your task is to extract the data from the image and format it into a structured JSON format like the one below '{\n  \"question\": {\n    \"id\": 2,\n    \"questionText\": \"Size of large data files can be reduced to save storage disk space. Which algorithm is appropriate to reduce size of large files?\",\n    \"topic\": \"Data Compression\",\n    \"difficultyLevel\": \"Medium\",\n    \"estimatedTime\": \"1 minute\",\n    \"choices\": [\n      {\n        \"choiceId\": \"a\",\n        \"text\": \"Merge sort algorithm\",\n        \"correct\": false,\n        \"explanation\": \"Merge sort is used for sorting data, not for compression.\"\n      },\n      {\n        \"choiceId\": \"b\",\n        \"text\": \"Huffman encoding algorithm\",\n        \"correct\": true,\n        \"explanation\": \"Huffman encoding is a lossless compression algorithm that reduces file size efficiently.\"\n      },\n      {\n        \"choiceId\": \"c\",\n        \"text\": \"Heap sort algorithm\",\n        \"correct\": false,\n        \"explanation\": \"Heap sort is a sorting algorithm, not related to file compression.\"\n      },\n      {\n        \"choiceId\": \"d\",\n        \"text\": \"Prim's algorithm\",\n        \"correct\": false,\n        \"explanation\": \"Prim's algorithm is used for finding minimum spanning trees in graphs, not for compression.\"\n      }\n    ],\n    \"correctAnswer\": {\n      \"choiceId\": \"b\",\n      \"reason\": \"Huffman encoding is the standard algorithm for reducing file size in lossless data compression.\"\n    }\n  }\n}\n'",
                ],
            }])
    # Get the response from the model
    response = chat_session.send_message("get the json for this\n")
    return response

# response = get_json_from_image("./Last Year National Exit Exam/test-data.jpg")
# print(response.text)
 
# open("output.json", "w").write(response.text)
