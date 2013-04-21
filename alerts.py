#Classes
#Alert

#Functions
#SendAlert

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from google.appengine.api import mail
from google.appengine.api import users

import models

#Process the Alert Request
class Alert(webapp.RequestHandler):
    def get(self):
        
        #Parse the request from the Arduino to determine if you
        #want an email alert or a text msg
        alertType=self.request.get('Type')
        
        #Call the SendAlert function and return the response to the Arduino
        self.response.out.write(SendAlert(alertType, 'This is a test alert'))
        
    def SendAlert(alertType, msg):
        #Get the UserPrefs entity using your email address at the key_name.
        #This address is hard-coded because App Enging can't tell who the
        #current user is from an Arduino request. You could pass this
        #in if you wanted to.
        UserPrefs = models.UserPrefs.get_or_insert('test@example.com')
        
        #Get the address from the entity based on the type of alert wanted
        if alertType=='email':
            address=UserPrefs.textAddress
        else:
            address=UserPrefs.textAddress
            
        #This sends the email.
        #A special note here-the SENDER address must be the address
        #you used to create the application, or an address you have
        #given administration privileges.
        mail.send_mail(
            sender=UserPrefs.emailAddress,
            to=address,
            subject='ADACS Alert',
            body=msg)
        
        #Message used as the response
        return('Message Sent')