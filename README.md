
# JobFinder

JobFinder is an online platform connecting job seekers and employers. It offers job listings, company details, and direct communication tools. JobFinder makes job hunting easier and more interactive for everyone involved.


## Local Environment Setup
#### Create a virtual environment:
```bash
# Using virtualenv
virtualenv virtualenv

# Using Python 3.8
python3.8 -m venv virtualenv
```
#### Activate the virtual environment:
```bash 
source venv/bin/activate
```
#### Clone the repository and install the required packages:
```bash
pip install -r requirements.txt
```
## Running the Project
#### Collect Static (Optional)
```bash
Note: Only necessary when debug is False (in production mode).
python manage.py collectstatic
```
#### Create Initial Database:
```bash
python manage.py migrate
```
#### Run Server:
```bash
python manage.py runserver
```
#### Default Django Admin Credentials:
```bash
Email: admin@admin.com
Password: admin
```
## Support the Project
If you find this project useful, show your support by starring it! 🌟
