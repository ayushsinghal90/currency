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

### Update ENV variables
- Add **FIXER_API_KEY** in docker-compose.yaml

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

## Running Http API 
- Get Rates Endpoint
~~~~
http://0.0.0.0:8000/rate/
~~~~
- Body
~~~~
{
    "pair":"EUR",
    "symbols": ["JPY","USD"]
}
~~~~

## Running GraphQl 
- Endpoint
~~~~
http://0.0.0.0:8000/graphql/
~~~~
- Query structure Example
~~~~
query getRates{
  rates(base: "EUR", symbols: ["JPY","USD","INR"]){
    base,
    rates {
      symbol,
      rate,
      base
    }
  }
}
~~~~
- Mutation structure Example
~~~~
mutation updateRates{
  updateRates(base: "EUR", symbols: ["JPY","USD","INR"]){
    ok,
    currencyRates{base,
    rates {
      symbol,
      rate,
      base
    }
    }
  }
}
~~~~

## Running test Cases
Use the following command to run test cases in all apps.

**Note**: current coverage **85%**
```bash
python manage.py test
```
