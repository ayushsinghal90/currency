# currency
# Introduction

This is a backend for a service that give rate between two currency
# Developer Guide

## Getting Started

### Prerequisites
- [python3.6](https://www.python.org/downloads/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](https://www.postgresql.org/download/)

### Initialize the project

Create and activate a virtualenv:
(Make sure to activate virtual environment with python version 3.6)

```bash
virtualenv --python=python3 venv
source venv/bin/activate
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

### Run
- Build container up
~~~~
docker-compose up
~~~~
- Bring container down
~~~~
docker-compose down
~~~~
- Hosted url
~~~~
http://0.0.0.0:8000
~~~~
