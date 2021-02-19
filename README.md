# Bookinder
This is KU Hackathon 2021. Team Name: Devs' Street

## Contributing

### Setting-up the project

  * Download and install Python 3.7
  * Download and install Git.
  * Fork the Repository.
  * Clone the repository to your local machine `$ git clone https://github.com/<your-github-username>/Bookinder.git`
  * Change directory to Bookinder `$ cd Bookinder`
  * Install virtualenv `$ pip3 install virtualenv`
  * Create a virtual environment `$ virtualenv env -p python3.7`  
  * Activate the env: `$ source env/bin/activate` (for linux) `> ./env/Scripts/activate` (for Windows PowerShell)
  * Install the requirements: `$ pip install -r requirements.txt`
  * Make migrations `$ python manage.py makemigrations`
  * Migrate the changes to the database `$ python manage.py migrate`
  * Create admin `$ python manage.py createsuperuser`
  * Run the server `$ python manage.py runserver`
  
 #### FrontEnd
 
  * Add your `html` files in the folder named `templates`.
  * Add your `css` files in the folder named `static`.
