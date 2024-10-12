# LabSense - Diagnostic Assistant

## Overview
LabSense is an AI-powered diagnostic assistant that helps doctors interpret lab test results by traversing clinical decision trees and providing diagnostic suggestions. This repository contains the backend (Flask) and frontend (React) code.

## Prerequisites
Before setting up the project, make sure you have the following installed:
- Python 3.x
- PostgreSQL
- Node.js and npm
- Git

## Setup Instructions

### 1. Clone the Repository
First, clone the repository:

git clone https://github.com/aryandgandhi/labx.git
cd labx

### 2\. Setting Up the Virtual Environment (venv)

#### a. Create a Virtual Environment

Create a virtual environment named `venv`:





`python3 -m venv venv`

#### b. Activate the Virtual Environment

-   On macOS/Linux:

    

    

    `source venv/bin/activate`

-   On Windows:

    

    

    `venv\Scripts\activate`

#### c. Install the Python Dependencies

With the virtual environment activated, install the required Python packages:





`pip install -r requirements.txt`

### 3\. Setting Up PostgreSQL Locally

#### a. Install PostgreSQL

If PostgreSQL is not installed on your system, follow these instructions:

-   **macOS**:

    

    

    `brew install postgresql
    brew services start postgresql`

-   **Linux**:

    

    

    `sudo apt-get install postgresql postgresql-contrib
    sudo service postgresql start`

-   **Windows**: Download the installer from the official PostgreSQL website and follow the setup instructions.

#### b. Create a Database for LabSense

Open the PostgreSQL command line tool:





`psql postgres`

Then create a new database and user:

sql



`CREATE DATABASE labsense;
CREATE USER flask_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE labsense TO flask_user;`

#### c. Set Up Environment Variables

Create a `.env` file in the root of the backend folder (`labx/`) with the following contents:





`DATABASE_URL=postgresql://flask_user:yourpassword@localhost:5432/labsense
SECRET_KEY=your_secret_key_here`

This `.env` file will store sensitive environment variables like the database connection URL and Flask secret key.

### 4\. Configuring the Flask Application

#### a. Update the Flask Configuration

Modify the `app.py` to read the database URL from the `.env` file:

python



`from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)`

#### b. Initialize the Database

Run the following commands to set up the initial database structure:





`flask db init
flask db migrate -m "Initial migration."
flask db upgrade`

### 5\. Running the Flask Backend

With everything configured, start the Flask development server:





`flask run`

The backend should now be running on `http://localhost:5000`.

### 6\. Setting Up the React Frontend

#### a. Navigate to the Frontend Directory

Change to the React frontend directory:





`cd labsense-frontend`

#### b. Install Dependencies

Install the required Node.js packages:





`npm install`

#### c. Start the Development Server

Run the React app:





`npm start`

The frontend should now be running on `http://localhost:3000`.

### 7\. Connecting Frontend to Backend

Make sure both the Flask backend (`http://localhost:5000`) and the React frontend (`http://localhost:3000`) are running. The React app will send requests to the Flask API for processing.

Important Commands
------------------

### Virtual Environment

-   **Activate venv**:
    -   macOS/Linux: `source venv/bin/activate`
    -   Windows: `venv\Scripts\activate`
-   **Deactivate venv**: `deactivate`

### Database

-   **Start PostgreSQL**:
    -   macOS: `brew services start postgresql`
    -   Linux: `sudo service postgresql start`
-   **Stop PostgreSQL**:
    -   macOS: `brew services stop postgresql`
    -   Linux: `sudo service postgresql stop`



Additional Notes
----------------

-   To reset the database, you can drop and recreate it:

    sql

    

    `DROP DATABASE labsense;
    CREATE DATABASE labsense;`

-   Make sure to add `.env` to `.gitignore` to avoid pushing sensitive information to version control.



4o

ChatGPT can make mistakes. Check important info.
