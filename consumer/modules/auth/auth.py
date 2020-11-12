from ...models import Users, LoginHistory
from .tokens import genToken
import datetime
from ..api_general import genUrl
from django.contrib.auth import authenticate

class Auth:
    def __init__(self, data):
        self.data=data

    def signUp(self):
        response={}
        payload={}
        
        try:
            # Check if username is available
            if Users.objects.filter(username=self.data['username']).exists() == True:
                raise Exception('Username available. Please choose another.')
            else:
                user=Users.objects.create_user(
                    full_names=self.data['fullNames'],
                    phone=self.data['phone'],
                    email=self.data['email'],
                    url=genUrl(),
                    username=self.data['username'],
                    password=self.data['password']
                )
                
                payload={
                    'id':user.url,
                    'exp':datetime.datetime.utcnow() + datetime.timedelta(weeks=4),
                    'iat':datetime.datetime.utcnow()
                }
                user.token=genToken(payload)
                user.save()
                response={
                    'status':1,
                    'message':'User entered successfully'
                }

        except Exception as e:
            response={
                'status':0,
                'message':'{}'.format(e)
            }
        return response

    def login(self):
        response={}
        try:
            userInstance=authenticate(username=self.data['username'], password=self.data['password'])
            if userInstance == None:
                raise Exception('Invalid credentials. Please try again')
            
            loginHistoryInstance= LoginHistory(user=userInstance, device_info=self.data['device_info'], location=self.data['location'])
            loginHistoryInstance.save()
            response={
                'status':1,
                'message':'Login successful',
                'token':userInstance.token,
                'login_id':loginHistoryInstance.id
            }

        except Exception as e:
            response={
                'status':0,
                'message':'{}'.format(e)
            }
        return response
