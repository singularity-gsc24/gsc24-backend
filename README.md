# GSC24

## Local Setup

> This project uses Python 3.11.x

### With Virutal Environment

Clone this repo and open the folder, then run the below to commands in the terminal to create a virtual environment.

```bash
#windows
py -m venv venv
```

```bash
#linux
python3 -m venv venv
```

Activate virutal environment

```bash
.\venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Perform database migrations

```bash
py manage.py makemigrations
py manage.py migrate
```

To run the project,

```bash
py manage.py runserver
```

Now visit `localhost:8000`
