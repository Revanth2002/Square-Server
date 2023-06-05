### Zero Subscribe Server

Clone this repo and run the following commands 
````bash
git clone https://github.com/Revanth2002/Square-Server.git
cd Square-Server
````
Change the secrets in the [settings.py](./squarebackend/settings.py) file
```python 
BASE_URL =  "http://localhost:8000" # your server url
SQUARE_APP_ID= "sandbox-****-***" # your square app id
SQUARE_APP_SECRET = "***" # your square app secret
SQUARE_API_URL = "https://connect.squareupsandbox.com"
SQUARE_SANDBOX_TOKEN = "*****" # your square sandbox token

```

To run the server you need to install the requirements and run the following command
```bash
pip install -r requirements.txt
python3 manage.py runserver 0.0.0.0:8000
```