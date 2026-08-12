# 🎬 Django Feedback & AI Analysis System

A full-stack Django web application for collecting movie feedback, storing it in MySQL, deploying the application to the cloud, and analyzing user feedback using Google's Gemini API.

The project was developed in **three stages**, progressing from a local Django + MySQL application to a cloud-deployed application with AI-powered feedback analysis.

---

## 🚀 Project Overview

This project allows users to:

* Submit movie feedback through a Django web form
* Store feedback in a MySQL database
* Deploy the application to the cloud
* Store production data using a cloud MySQL database
* Analyze movie reviews using Google's Gemini API
* Generate:

  * Sentiment
  * Review summary
  * Suggestions for the director
* Store the AI-generated analysis back in the database

### Project Architecture

```text
User
  │
  ▼
Django Web Application
  │
  ├── Feedback Form
  │       │
  │       ▼
  │   MySQL Database
  │
  └── AI Analysis
          │
          ▼
      Gemini API
          │
          ▼
   Sentiment / Summary / Suggestions
          │
          ▼
      MySQL Database
```

---

# 🏗️ Development Stages

## Stage 1 — Local Django + MySQL

The initial version was developed and tested locally.

```text
Django
   │
   ▼
Feedback Form
   │
   ▼
Local MySQL Database
```

The application collects:

* Name
* Age
* Movie
* Email
* Movie feedback

The submitted information is saved into MySQL using Django's ORM.

---

## Stage 2 — Cloud Deployment

The application was then prepared for cloud deployment.

```text
User
  │
  ▼
Django Application
  │
  ▼
Render
  │
  ▼
Cloud MySQL Database
```

### Cloud Technologies

* **Render** — Application deployment
* **Aiven MySQL** — Cloud database
* **Gunicorn** — Production WSGI server
* **WhiteNoise** — Static file serving

Environment variables are used for database credentials and other sensitive configuration instead of hardcoding secrets in the source code.

---

## Stage 3 — Gemini AI Feedback Analysis

The final stage adds AI-powered analysis using Google's Gemini API.

A submitted movie review can be analyzed to generate:

```text
Movie Review
     │
     ▼
Gemini API
     │
     ├── Sentiment
     ├── Summary
     └── Suggestions
```

The generated results are stored in the same database.

### Example

```json
{
  "sentiment": "Positive",
  "summary": "The reviewer enjoyed the movie and praised its storytelling.",
  "suggestions": "Consider improving the pacing of the second half."
}
```

The database tracks whether a feedback record has already been analyzed using the `is_analyzed` field.

---

# 🛠️ Tech Stack

## Backend

* Python
* Django 5.2
* Django ORM
* REST-style JSON response handling

## Database

* MySQL
* Aiven MySQL
* Django migrations

## AI

* Google Gemini API
* `google-genai`
* Gemini-powered sentiment and feedback analysis

## Deployment

* Render
* Gunicorn
* WhiteNoise

## Configuration

* Python Dotenv
* Environment variables

## Frontend

* HTML
* Django Templates

---

# 📁 Project Structure

```text
feedbacksqlproject/
│
├── feedbacksqlproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_feedback_is_analyzed_feedback_sentiment_and_more.py
│   │   └── __init__.py
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

---

# 🗄️ Database Model

The main `Feedback` model contains:

| Field         | Type         | Description                             |
| ------------- | ------------ | --------------------------------------- |
| `id`          | AutoField    | Unique feedback ID                      |
| `name`        | CharField    | User name                               |
| `age`         | IntegerField | User age                                |
| `movie`       | CharField    | Movie name                              |
| `email`       | EmailField   | User email                              |
| `feed`        | TextField    | Movie feedback                          |
| `sentiment`   | CharField    | AI-generated sentiment                  |
| `summary`     | TextField    | AI-generated review summary             |
| `suggestions` | TextField    | AI-generated suggestion                 |
| `is_analyzed` | BooleanField | Tracks whether AI analysis is completed |

---

# 🔄 Application Flow

### 1. Submit Feedback

The user enters movie information and feedback through the Django form.

### 2. Validate Form

Django validates the submitted form data.

### 3. Save to Database

The validated feedback is saved using Django's ORM.

### 4. AI Analysis

When AI analysis is requested, the application retrieves the feedback and sends the movie review to Gemini.

### 5. Process AI Response

The application receives a JSON response containing:

* Sentiment
* Summary
* Suggestions

### 6. Store Results

The AI-generated information is saved back to the corresponding feedback record.

---

# 🔌 API Endpoint

The project exposes an endpoint for triggering AI analysis:

```text
POST /analyze/<feedback_id>/
```

Example:

```text
POST /analyze/1/
```

The endpoint returns a JSON response.

### Successful Response

```json
{
  "status": "success",
  "data": {
    "sentiment": "Positive",
    "summary": "The reviewer enjoyed the movie.",
    "suggestions": "Consider improving the pacing."
  }
}
```

---

# ⚙️ Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/tarunreddykalluri/tarun_django_project_feedback.git
cd tarun_django_project_feedback
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key

DB_NAME=feedbackdb
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

> Never commit `.env` to GitHub. The project `.gitignore` excludes environment files.

## 5. Apply Migrations

```bash
python manage.py migrate
```

## 6. Run Django

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/feed/
```

---

# ☁️ Deployment

The application can be deployed using:

```text
GitHub
   │
   ▼
Render
   │
   ├── Django
   ├── Gunicorn
   └── WhiteNoise
          │
          ▼
      Aiven MySQL
```

For production deployment, configure the required environment variables in the hosting platform instead of committing credentials to the repository.

---

# 🔐 Security

Sensitive information is intentionally kept outside the source code.

The application uses environment variables for:

* Gemini API key
* Django secret key
* Database username
* Database password
* Database host
* Database name
* Database port

Example:

```python
os.environ.get("GEMINI_API_KEY")
```

and:

```python
os.environ.get("DB_PASSWORD", "")
```

The `.env` file is excluded through `.gitignore`.

---

# 🧪 Validation

The project can be checked using Django's built-in system checks:

```bash
python manage.py check
```

Expected result:

```text
System check identified no issues (0 silenced).
```

Database migrations can be inspected using:

```bash
python manage.py showmigrations
```

---

# 📌 Key Features

* ✅ Django-based web application
* ✅ Feedback collection using Django Forms
* ✅ MySQL database integration
* ✅ Django ORM
* ✅ Database migrations
* ✅ Cloud deployment architecture
* ✅ Aiven MySQL integration
* ✅ Render deployment support
* ✅ Gemini API integration
* ✅ AI sentiment analysis
* ✅ AI-generated summaries
* ✅ AI-generated suggestions
* ✅ JSON-based AI response handling
* ✅ Environment-based secret management
* ✅ Production static-file handling with WhiteNoise

---

# 📈 Future Improvements

Possible future enhancements include:

* User authentication and authorization
* Pagination for feedback records
* Admin dashboard for analytics
* Graphical sentiment statistics
* Bulk AI analysis
* Improved AI response validation
* Background processing for AI analysis
* REST API using Django REST Framework
* Automated testing
* CI/CD pipeline

---

# 👨‍💻 Author

**Tharun Kumar Reddy Kalluri**

B.Tech Graduate | Python | Django | MySQL | AI/ML

GitHub:
https://github.com/tarunreddykalluri

Portfolio:
https://www.tarunreddykalluri.com

---

## 📄 License

This project is intended for educational and portfolio purposes.
