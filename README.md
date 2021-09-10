# Video Library
# Introduction

A video library that stores YouTube videos.
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

### Api Collection
- [API collection](https://drive.google.com/file/d/13FNxLKe4PmorAuXJ1w39aAR89dbGQeWy/view?usp=sharing)
- [ENV collection](https://drive.google.com/file/d/1KE90Wx4DnkCo-7rOEQSjPZdayzDqzLqc/view?usp=sharing)

### Add YouTube api key
- Url
~~~
http://0.0.0.0:8000/keys/
~~~
- body  **(key will expire after 22 jun 11am)**
~~~
{
    "type": "youtube",
    "key": "AIzaSyAQiK5eDBZwv0OO2uV4J-n_BqDbKHpHKYU"
}
~~~

### Change YouTube schedule query config
- change **SEARCH_KEYWORD** currently **entertainment**
- change **SCHEDULED_QUERY_TIME** currently **700 minutes**