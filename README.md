# cloudini

Prerequisites:
1. Install python 3 (the current latest is 3.8.2, which is definitely good enough) (https://www.python.org/downloads/)
2. Install git bash (git command line for windows) (https://git-scm.com/downloads)
3. Install Pycharm from Jetbrains offical website (use colman tutorial to activate the ultimate version http://db.cs.colman.ac.il/Downloads/jetbrains.pdf)


We are going to work with the standard git flow, which means:
We are going to have two main branches - Master and Development
Master branch - no one can touches the master
Development branch - every feature will be checked out from development, and of course, will be pushed back into development

* More information about git flow can be found here - https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow

New features:
- Clone this repo (using git clone)
- Checkout to development branch (git checkout development)
- Create you new Feature Branch (git checkout -b <my_fb_name>)
- Activate the virtual env (venv\Scripts\activate)
- Now you will be able to run the server locally (python manage.py runserver, using this command you can also change the access list and the port)
- Develop your code and test it locally (you can push it to your own feature branch using - git add & git commit & git push)

When you done with your feature - we will push it together to development:
- First - we will rebase it from development to align the branch and get all the missed commits (git pull --rebase origin development)
- Handle the conflicts
- Hard push (git push -f)
- Then, open a Pull Request (using the Git UI)

* Look for a git tutorial for better understand this flow (and this approach)


====================================

For being able to work with the DB locally:
Download and install PostgreSQL (9.6.X version) - https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
set the Password to - Aa123456!
To update your local DB with the relevant tables - after cloning the repo and checking out to your parituclar branch, run:
* pip install psycopg2
* python manage.py makemigrations
* python manage.py migrate

Then, log in to your local DB (using pgadmin) and make sure that the cloudinis tables created (you should see 4 tables - customer, policy, activatedpolicy and violation)

