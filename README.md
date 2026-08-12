# Django Feedback & AI Analysis System

A Django-based web application for collecting movie feedback, storing the data in MySQL, deploying the application to the cloud, and performing AI-based analysis of movie reviews using the Google Gemini API.

The project was developed in three stages:

1. Local Django application with MySQL
2. Cloud deployment using Render and Aiven MySQL
3. AI-powered feedback analysis using the Google Gemini API

## Project Overview

The application allows users to submit movie feedback through a Django web form.

The submitted information is stored in a MySQL database. The application can then analyze the movie review using the Gemini API and store the generated analysis in the database.

The AI analysis produces:

* Sentiment
* Review summary
* Suggestion for the director

The project demonstrates the integration of web development, database management, cloud deployment, and generative AI in a single application.

## Development Stages

### Stage 1: Local Django and MySQL

The initial version was developed and tested locally using Django and MySQL.

Application flow:

```text
User
  |
  v
Django Feedback Form
  |
  v
Django ORM
  |
  v
Local MySQL Database
```

The feedback form collects:

* Name
* Age
* Movie
* Email
* Feedback

The submitted data is validated using Django Forms and stored using Django's ORM.

### Stage 2: Cloud Deployment

The application was then configured for cloud deployment.

```text
User
  |
  v
Django Application
  |
  v
Render
  |
  v
Aiven MySQL
```

Technologies used during deployment:

* Render for application hosting
* Aiven MySQL for cloud database storage
* Gunicorn for serving the Django application
* WhiteNoise for static file handling

Database credentials and other sensitive configuration values are loaded through environment variables rather than being stored directly in the source code.

### Stage 3: AI Feedback Analysis

The final stage integrates the Google Gemini API to analyze movie reviews.

Application flow:

```text
Stored Movie Feedback
        |
        v
    Gemini API
        |
        v
+----------------------+
| Sentiment            |
| Summary              |
| Suggestions          |
+----------------------+
        |
        v
MySQL Database
```

The application sends the movie name and review to Gemini and requests a JSON response containing the analysis.

The generated information is then stored in the corresponding `Feedback` database record.

## Tech Stack

### Backend

* Python
* Django 5.2
* Django Forms
* Django ORM

### Database

* MySQL
* Aiven MySQL
* Django Migrations

### AI

* Google Gemini API
* Google GenAI Python SDK

### Deployment

* Render
* Gunicorn
* WhiteNoise

### Configuration

* Python Dotenv
* Environment Variables

### Frontend

* HTML
* Django Templates

## Project Structure

```text
feedbacksqlproject/
|
├── feedbacksqlproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_feedback_is_analyzed_feedback_sentiment_and_more.py
│   │
│   ├── templates/
│   │   └── myapp/
│   │       ├── input.html
│   │       ├── output.html
│   │       └── response.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   └── views.py
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Database Model

The main database table is represented by the Django `Feedback` model.

| Field         | Type         | Purpose                                    |
| ------------- | ------------ | ------------------------------------------ |
| `id`          | BigAutoField | Unique feedback identifier                 |
| `name`        | CharField    | Name of the user                           |
| `age`         | IntegerField | Age of the user                            |
| `movie`       | CharField    | Movie name                                 |
| `email`       | EmailField   | User email                                 |
| `feed`        | TextField    | Submitted movie feedback                   |
| `sentiment`   | CharField    | AI-generated sentiment                     |
| `summary`     | TextField    | AI-generated review summary                |
| `suggestions` | TextField    | AI-generated suggestion                    |
| `is_analyzed` | BooleanField | Indicates whether AI analysis is completed |

## Application Flow

### Feedback Submission

1. User opens the feedback form.
2. User enters the movie and feedback details.
3. Django validates the submitted form.
4. The feedback is saved to MySQL.
5. The saved feedback can then be analyzed using the AI endpoint.

### AI Analysis

1. The application retrieves the selected feedback record.
2. The movie name and review are sent to Gemini.
3. Gemini returns the requested analysis in JSON format.
4. The application parses the JSON response.
5. Sentiment, summary, and suggestions are saved to the database.
6. `is_analyzed` is updated to `True`.
7. A JSON response is returned to the client.

## AI Analysis Endpoint

The application provides an endpoint for analyzing an individual feedback record:

```text
POST /analyze/<feedback_id>/
```

For example:

```text
POST /analyze/1/
```

A successful response follows this structure:

```json
{
    "status": "success",
    "data": {
        "sentiment": "Positive",
        "summary": "Example review summary",
        "suggestions": "Example suggestion"
    }
}
```

## Environment Variables

Sensitive values are not stored directly in the source code.

The application uses environment variables for configuration.

Example local `.env` file:

```env
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key

DB_NAME=feedbackdb
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

The `.env` file is excluded from Git using `.gitignore`.

For cloud deployment, the corresponding environment variables can be configured through the hosting platform.

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tarunreddykalluri/tarun_django_project_feedback.git
cd tarun_django_project_feedback
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and add the required database and Gemini API configuration.

Do not upload this file to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Run the Application

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/feed/
```

## Project Validation

Django's built-in system check can be used to verify the project configuration:

```bash
python manage.py check
```

Expected result:

```text
System check identified no issues (0 silenced).
```

Migration status can be checked using:

```bash
python manage.py showmigrations
```

## Security Considerations

The project does not store sensitive credentials directly in the source code.

Environment variables are used for:

* Django secret key
* Gemini API key
* Database username
* Database password
* Database host
* Database name
* Database port

The `.gitignore` file excludes environment files and Python cache files from version control.

## Future Improvements

Potential improvements include:

* Adding user authentication
* Adding pagination for feedback records
* Creating an analytics dashboard
* Displaying sentiment statistics using charts
* Adding automated tests
* Adding better validation for AI responses
* Adding background processing for AI analysis
* Building a REST API using Django REST Framework
* Adding CI/CD automation

## Author

**Tharun Kumar Reddy Kalluri**

B.Tech Graduate

GitHub: https://github.com/tarunreddykalluri


## License

This project was developed for educational and portfolio purposes.
