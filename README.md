# GSC24

## Finguard

Finguard is a project dedicated to the conservation of exotic and endangered fish species. Its goal is to facilitate the sustainable fishing practices by providing fishermen with information about fish species that are safe to hunt and fish, thus contributing to the preservation of marine biodiversity.

## Objective

The main objective of Finguard is to promote the conservation of exotic and endangered fish species by offering fishermen a platform where they can access reliable information about which fish species are safe to catch without endangering their populations.

## How It Works

Finguard achieves its goal by:

1. Providing a database of fish species along with their current conservation status.
2. Offering information on the locations where these fish species can be found.
3. Advising fishermen on sustainable fishing practices and suggesting alternative species to target, by providing the location of the fish species which are safe to hunt.

## Contribution to UN Sustainable Development Goals

Finguard directly contributes to the United Nations Sustainable Development Goal (UN SDG) 14: Life Below Water, by promoting the conservation and sustainable use of marine resources. By helping fishermen make informed decisions about which fish species to target, Finguard supports efforts to protect marine biodiversity and ensure the long-term health of our oceans.



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
