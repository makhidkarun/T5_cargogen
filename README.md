# T5_cargogen
Traveller 5 cargogen

Python modules to produce speculative cargoes in Traveller 5.

Current status:
- T5_cargogen.app.simple.TradeCargo() handles generating, naming, cost and price for a cargo
- T5_cargogen.app.simple.BrokerSale() hadnles broker interactions
- There is a web UI using flask. See notes for setting this up locally. Alternatively,
there is a copy in Heroku's app service at http://t5-cargogen.herokuapp.com/ Note that this uses Heroku's free tier, so you may encounter a short delay as the instance spins up (if it's already running, you should see it immediately).
- It has been extensively tested using Python 2.7, testing with Python 3.5 is in progress


## Running the Flask app

### Install Python virtualenv. 
Check your OS for instructions; here are some examples:
- Ubuntu: `sudo apt install python-virtualenv`
- CentOS: `sudo yum install python-virtualenv`
- Windows: See http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/
- Mac: `sudo easy_install virtualenv`


### Retrieve the code
Clone the repo with your preferred git client

Change to the newly-downloaded directory

### Prepare your Python venv
`$ virtualenv venv` This sets up a subdirectory called venv which will hold your virtual Python environment, including all the required Flask modules

### Start the server
```
$ python ./manage.py runserver
145 werkzeug _log():  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
5321 werkzeug _log(): 127.0.0.1 - - [25/Sep/2017 17:27:12] "POST / HTTP/1.1" 200 -
```

### Generate cargoes
Point a browser at localhost:5000 and enter a valid UWP in the *Source world UWP* box; under *Planet details* you will see your UWP, its relevant trade codes and the cargo, with label, description and cost/ton.

![screenshot](https://github.com/egor045/image_bank/raw/master/T5_cargogen-screenshot.png)

Add one or more UWPs (space- or comma-separated) to the *Market world UWP* box; under *Planet details* you will see the source world cargo as before, as well as a line for each market world listing its UWP, trade codes and the base sale price - the price that will be adjusted by an actual value Flux roll (see T5 rules, page 487).
 
## To do
- Make Python packages
- Generate actual value (based on market world and broker skill)
