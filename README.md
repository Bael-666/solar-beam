# solar-beam
Solar Beam app

#### How to export virtual environment: ####

pip freeze > requirements.txt

Then push the requirements.txt file to anywhere you want to deploy the code, and then just do what you did on dev machine -

$ virtualenv <env_name>
$ source <env_name>/bin/activate
(<env_name>)$ pip install -r path/to/requirements.txt

And there you have all your packages installed with the exact version.

