django-admin startproject authproject
create venv inside authproject directory
install django
create app
add urls.py to app
add database,static ,media root  to settings
add app to installed app to settings
run server
make migrations and migrate
add app path to urls.py inside projetdir(project auth)

####authapp(userapp)(seller)
go to authapp (user application folder)
create templates directory/seller> create basic.html for common html content for all htmlpage
create index.html for home page
go to views.py create function for index.html for home page
go to urls.py create url path for index.html for home page
complete index.html
 
create sinup_seller.html page for seller
creste signup_user.html for baseuser
create login.html for login page

###rootapp
go to rootapp create managers.py 
create customusermanager class parent Baseusermanger
create user ,superuser,

go to rootapp models.py create models for signupseller ,signupuser, login
lowercase emailfield, customuser,

goto rootapp create forms.py    
create registrationForm,UserForm , SellarForm classes

add AUTH_USER_MODEL = 'rootapp.CustomUser' to settings
makemigrations rootapp
migrate rootapp
##authapp
goto authapp view crate function or class for  signup page
###rootapp(adminapp)
create templatetag as a package inside rootapp
create __init__.py and myfilters.py inside templatetag
add {% load myfilters %} to signup page, login.html 
add form tag to login.html andd signup.html (user)

****sign up working >> put credential to database







################################
goto rootapp create mixins.py
go to urls.py create url path for login.html
go to views.py create class loginviewuser for login.html
add link to login.html


go to apps.py > create appconfig
go to models.py >  don't create appmodels
go to test.py > don't create tests for now