# reference
## https://medium.com/analytics-vidhya/deploying-a-streamlit-and-opencv-based-web-application-to-heroku-456691d28c41

## Preapration for heroku deployment

# preapare "requirements.txt" and "Aptfile(Only for opencv)" for uploading dependent module 
# pip install -r requirements.txt
# Aptfile is automatically being installed after requirements.txt are installed

# prepare "Procfile" and "runtime.txt" for web:app initilization and defining running python version

## Heroku configuration
# from setting/Buildpacks 
# add heroku/python and https://github.com/heroku/heroku-buildpack-apt

## After git init 
## Heroku Git Commands  (heroku-cli)

# heroku login
# heroku git:remote -a streamlit-opencv-demo
# git add .
# git commit -am "Commit message" 
# git branch -m master (if branch is not master,, for github brach should be main to push)
# git push heroku master (branch should be master for heroku)
# heroku ps:scale web=1 (Scale up the dynos in order to ensure smooth running of the application.)
# heroku open (This will open the application in the browser)

