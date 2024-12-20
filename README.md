
# Django Quiz Application

This is a simple Django-based quiz application that allows users to take a quiz, with questions and answers stored in the database.

## Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.6 or higher**
- **pip** (Python package manager)

## Project Setup

### Step 1: Set up a Virtual Environment

To keep the project dependencies isolated, create a virtual environment:

```bash
python -m venv myenv

```
```bash
myenv\Scripts\activate
```

### Step 2:Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3:Set Up the Database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```


### Step 4: Create a Django App
```bash
python manage.py startapp quiz
```

### Step 5:Run the Development Server
```bash
python manage.py runserver
```

#### https://quiz-application-lake.vercel.app/

![Alt text](https://github.com/Prajwal07523/Quiz-application/blob/bea25a2a05c7393290aa0ce6bcf79f5421d88bee/media/Home.png)
![Alt text](https://github.com/Prajwal07523/Quiz-application/blob/bea25a2a05c7393290aa0ce6bcf79f5421d88bee/media/Question.png)
![Alt text](https://github.com/Prajwal07523/Quiz-application/blob/bea25a2a05c7393290aa0ce6bcf79f5421d88bee/media/Result.png)
![Alt text](https://github.com/Prajwal07523/Quiz-application/blob/bea25a2a05c7393290aa0ce6bcf79f5421d88bee/media/Result2.png)








