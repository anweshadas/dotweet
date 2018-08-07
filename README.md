It is command line application for twitter using Python.

### Development

This project uses [pipenv](https://docs.pipenv.org) to manage all dependencies.
This is a Python3 project. 
This uses [click](http://click.pocoo.org/5/) to create command line application in Python.
This also uses [python-twitter](https://python-twitter.readthedocs.io/en/latest/index.html).

### Code formatting

I am using [Black](https://black.readthedocs.io/en/stable/) tool for code formatting. 

### Usage

We need a *config.json* for keeping all the configuration value to make the code work. One can get the values required from the developers account of Twitter. The following is an example *config.json* -
 
 ```
 {
    "access_token": "xxxx",
    "access_token_secret": "xxxx",
    "consumer_key": "xxxx",
    "consumer_secret": "xxxx",
    "user_numeric_id": "xxxx"
}
```
### License: 

GPLv3+