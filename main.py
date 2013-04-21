#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#Start of Step 4
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from google.appengine.api import users

import models #as of 11:30 AM 4/21/13, we do not yet have models.py
#End of Step 4
import webapp2

#Loads the HTML of the webapp 

class MainPage(webapp.RequestHandler): #(also step 4)
    def get(self):
        
        html = template.render('templates/header.html',{'title': 'Alert System'})
        html = html+template.render('templates/footer.html',{})
        
        self.response.out.write(html)

#Processes the JavaScript requests
class SaveAddress(webapp.RequestHandler):
    def get(self):
        #1. Parse the request
        address=self.request.get('Address')
        addressType=self.request.get('Type')
        
        #2. Use your user email address to get the UserPrefs entity
        #Your address is used as the key name. If the entity doesn't
        #exist, it is created.
        user=users.get_current_user()
        UserPrefs=models.UserPrefs.get_or_insert(str(user.email()))
        
        #3. Based on the addressType, set the UserPrefs property
        if addressType=='email':
            UserPrefs.emailAddress=address
        else:
            UserPrefs.textAddress=address
            
        #4. Put the entity in the datastore
        UserPrefs.put()
        
        #5. Return a response
        self.response.out.write('Saved')
