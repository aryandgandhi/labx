# LabSense - Diagnostic Assistant

## Overview
LabSense is an AI-powered diagnostic assistant that helps doctors interpret lab test results by traversing clinical decision trees and providing diagnostic suggestions. This repository contains the backend (Flask) and frontend (React) code.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Setting Up the Virtual Environment](#2-setting-up-the-virtual-environment-venv)
  - [3. Setting Up PostgreSQL Locally](#3-setting-up-postgresql-locally)
  - [4. Configuring the Flask Application](#4-configuring-the-flask-application)
  - [5. Running the Flask Backend](#5-running-the-flask-backend)
  - [6. Setting Up the React Frontend](#6-setting-up-the-react-frontend)
  - [7. Connecting Frontend to Backend](#7-connecting-frontend-to-backend)
- [Important Commands](#important-commands)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Prerequisites
Before setting up the project, make sure you have the following installed:
- Python 3.x
- PostgreSQL
- Node.js and npm
- Git

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/aryandgandhi/labx.git
cd labx
```

### 2. Setting Up the Virtual Environment (venv)

a. Create a Virtual Environment
```bash
python3 -m venv venv
```

b. Activate the Virtual Environment
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

c. Install the Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setting Up PostgreSQL Locally

a. Install PostgreSQL
- **macOS**: 
  ```bash
  brew install postgresql
  brew services start postgresql
  ```
- **Linux**:
  ```bash
  sudo apt-get install postgresql postgresql-contrib
  sudo service postgresql start
  ```
- **Windows**: Download the installer from the official PostgreSQL website and follow the setup instructions.

b. Create a Database for LabSense
```sql
psql postgres
CREATE DATABASE labsense;
CREATE USER flask_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE labsense TO flask_user;
```

c. Set Up Environment Variables
Create a `.env` file in the root of the backend folder (`labx/`) with the following contents:
```
DATABASE_URL=postgresql://flask_user:yourpassword@localhost:5432/labsense
SECRET_KEY=your_secret_key_here
```

### 4. Configuring the Flask Application

a. Update the Flask Configuration
Modify the `app.py` to read the database URL from the `.env` file:
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
```

b. Initialize the Database
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 5. Running the Flask Backend
```bash
flask run
```
The backend should now be running on `http://localhost:5000`.

### 6. Setting Up the React Frontend

a. Navigate to the Frontend Directory
```bash
cd labsense-frontend
```

b. Install Dependencies
```bash
npm install
```

c. Start the Development Server
```bash
npm start
```
The frontend should now be running on `http://localhost:3000`.

### 7. Connecting Frontend to Backend
Ensure both the Flask backend (`http://localhost:5000`) and the React frontend (`http://localhost:3000`) are running. The React app will send requests to the Flask API for processing.

## Important Commands

### Virtual Environment
- **Activate venv**:
  - macOS/Linux: `source venv/bin/activate`
  - Windows: `venv\Scripts\activate`
- **Deactivate venv**: `deactivate`

### Database
- **Start PostgreSQL**:
  - macOS: `brew services start postgresql`
  - Linux: `sudo service postgresql start`
- **Stop PostgreSQL**:
  - macOS: `brew services stop postgresql`
  - Linux: `sudo service postgresql stop`

## Project Structure
```
labx/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
├── .env
├── .gitignore
└── README.md
```

## Contributing
We welcome contributions to LabSense! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our code of conduct and the process for submitting pull requests.

## Troubleshooting
- If you encounter database connection issues, ensure PostgreSQL is running and the `.env` file contains the correct credentials.
- For frontend-backend connection problems, check that both servers are running and the React app is configured to send requests to the correct backend URL.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
