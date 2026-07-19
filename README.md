# AI Meeting Intelligence Platform

A Django-based web application for uploading meeting recordings, transcribing them, and generating AI-powered summaries and insights. The platform is organized around meetings, agents, dashboards, and account management.

## Features

- Upload meeting audio/video files
- Store meeting metadata and media files
- Transcribe meetings using AI transcription workflows
- Generate summaries and structured meeting insights
- View results through a simple dashboard interface

## Project Structure

- accounts/ - user account and authentication related logic
- agents/ - transcription and summarization agent modules
- ai_engine/ - AI processing components
- dashboard/ - dashboard views and routes
- meetings/ - meeting upload, models, and result handling
- templates/ - HTML templates for the web UI
- static/ - CSS, JavaScript, and images

## Tech Stack

- Python
- Django
- SQLite
- HTML/CSS/JavaScript
- Django REST Framework

## Requirements

Make sure Python is installed on your system.

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If a requirements file is not present, install the essentials manually:

   ```bash
   pip install django djangorestframework
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser at:

   ```text
   http://127.0.0.1:8000/
   ```

## Usage

- Upload a meeting file from the web interface
- Wait for processing to complete
- Review the generated transcription and summary in the results page

## Notes

This project is currently a development/demo application and may require additional configuration for production use, including secure settings, authentication hardening, and deployment setup.

## License

This project is provided for educational and demonstration purposes.
