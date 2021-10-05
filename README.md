#WierdText

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Local Setup](#local-setup)
* [Heroku Setup](#heroku-setup)
* [How to use app](#how-to-use-app)


## General info
WierdText is a simple API with encoder and decoder.

Encoder, as a name suggests, encode messages.
For each original word in the original text, the first and last character
remains unchanged, but all the characters in the middle of the word shuffles.
Whitespace, punctuation, etc. stays like in the original.
Words that got shuffled are saved as a sorted list of original words (only
include words that got shuffled, not text that did not).

Decoder decodes encoded messages.
Decoder uses list of original words to restore them from encoded version.
	
## Technologies
Project is created with:
* python==3.9.0
* heroku==7.59.0
* pytest==6.2.5
* Flask==2.0.2
* Flask-RESTful==0.3.9
* gunicorn==20.1.0
	
## Local Setup
To run this project locally:

1. Create a virtualenv(https://docs.python.org/3/library/venv.html)

2. Install requirements:
```
$ pip install requirements.txt
```

3. Run a Flask:
```
$ export FLASK_APP=flaskapp
$ flask run
```


## Heroku Setup
To run this project on Heroku:


1. Install heroku and create an account
(https://devcenter.heroku.com/articles/heroku-cli):

2. Login on heroku:
```
$ heroku login
```

3. Create url:
```
$ heroku create
```

4. Push git repository to heroku:
```
$ git push heroku master
```


## How to use app

To use Encoder or Decoder, you need to send a POST request:

Encoder: ```https://{your custom site name}.herokuapp.com/v1/encode```

Decoder: ```https://{your custom site name}.herokuapp.com/v1/decode```

---------------------------------------------------
As a body of request use json. For Encoder it should look like this:
```
{"sentence": "Hello Word"}
```
Expected output: ```"\n—weird—\nHlelo Wrod\n—weird—\nHello Word"```

---------------------------------------------------
For Decoder request should look like this:
```
{"sentence": "\n—weird—\nHlelo Wrod\n—weird—\nHello Word"}
```
Expected output: ```"Hello Word"```
