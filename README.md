# Quiz App DB seeder

This project is a Quiz App DB seeder script that extracts multiple-choice questions from images and stores them in a database. The script uses Google Gemini API for image processing and Supabase and Appwrite for database management.

## Features

- Extracts multiple-choice questions from images.
- Stores questions in Supabase and Appwrite databases.
- Supports various question formats and topics.

## Project Structure

- `db_preparation/`
    - `.gitignore`: Specifies files and directories to be ignored by Git.
    - `main.py`: Contains the main logic for uploading files to Gemini and extracting questions.
    - `output.json`: Example output of extracted questions in JSON format.
    - `supabase_script.py`: Script for inserting questions into Supabase.
    - `upload_appwrite.py`: Script for uploading extracted questions to Appwrite.
    - `create_collection.py`: Script for creating collections and inserting documents in Appwrite.
    - `__init__.py`: Empty file to mark the directory as a Python package.
- `.env.example`: Example environment variables file.
- `.env`: Environment variables file (not included in version control).

## Setup

1. Clone the repository:
     ```sh
     git clone https://github.com/Chaos-19/quiz_app_db_seeder.git
     cd quiz_app_db_seeder
     ```

2. Create a virtual environment and activate it:
     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

3. Install the required packages:
     ```sh
     pip install -r requirements.txt
     ```

4. Copy the `.env.example` to `.env` and fill in the required credentials:
     ```sh
     cp .env.example .env
     ```

5. Run the scripts to process images and upload questions:
     ```sh
     python db_preparation/main.py
     python db_preparation/upload_appwrite.py
     ```

## Usage

- To extract questions from an image and get the JSON format:
    ```py
    from main import get_json_from_image
    response = get_json_from_image("path_to_image.jpg")
    print(response.text)
    ```

- To insert questions into Supabase:
    ```py
    from supabase_script import create_document
    create_document(question_data)
    ```

- To upload questions to Appwrite:
    ```py
    from upload_appwrite import list_files_in_directory
    files = list_files_in_directory("path_to_directory")
    ```

## Environment Variables

- `GEMINI_API_KEY`: API key for Google Gemini.
- `SUPABASE_URL`: URL for Supabase.
- `SUPABASE_KEY`: API key for Supabase.
- `APPWRITE_ENDPOINT`: Endpoint for Appwrite.
- `PROJECT_ID`: Project ID for Appwrite.
- `DATABASE_ID`: Database ID for Appwrite.
- `COLLECTION_ID`: Collection ID for Appwrite.

## License

This project is licensed under the MIT License.