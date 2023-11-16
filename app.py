from flask import Flask,request,render_template
import requests

app=Flask(__name__)  
# https://purple-actor-taxdu.pwskills.app:5002 

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weatherapp', methods=['GET', 'POST'])
def get_weatherdata():
    url='https://api.openweathermap.org/data/2.5/weather'
    param={'q':request.form.get('city'),'appid':request.form.get('appid'),'units':request.form.get('units')}
    response=requests.get(url,params=param)
    data=response.json()
    city=data['name']
    return f'data : {data}  city:{city}'
    



if __name__=='__main__': 
    app.run(host='0.0.0.0',port=5002)

# If you're currently in the Python shell, type exit() and 
# press Enter to exit the shell and return to your system's command line.And then 
# type 'pip install requests'
# use 'ctrl l' to clear the terminal 
# now this code is working very well so our step is to deploy this thing inside cloud through github 
# in this lab everything is preinstalled but when deploy things on the cloud (cloud always gives you a blank system) we have to 
# install libraries over there.keeping that in mind we have 'requirements.txt' and this will be used to keep all the dependencies
# or libraries and will in help in installing them in the cloud system easily
# and then we will push our code from "local system" to "github" and then to "cloud"
# on the terminal in the 'weather_app' now type 'git init'  
# then  git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/rk24101/18_22Oct_weatherapprepo-.git
# git push -u origin main
# this will push your all thing in 'weather_app' folder in the github repository
# to clone from github repository we need to type 'git clone url_to_clone_from_git_repository'
# in the python terminal
# now we have deploy in the cloud from the github,we are using "render.com" for cloud
