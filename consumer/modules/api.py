from .auth.auth import Auth
from ..models import Users, LoginHistory, Category, Services, Packages
from .api_general import genUrl
from django.core.files import File

class API:

    def __init__(self, data):
        self.data=data

    def api(self):
        responseData={}

        if self.data['activityID'] == 'signUp':
            responseData=Auth(self.data['requestData']).signUp()

        if self.data['activityID'] == 'login':
            responseData=Auth(self.data['requestData']).login()

        if self.data["activityID"] == "getCategories":
            try:
                categories=Category.objects.filter(visibility=1).values("id","name")
                responseData={
                    "status":1,
                    "data":categories
                }
            except:
                responseData={
                    "status":0,
                    "message":"Error retrieving categories. Please try again later"
                }

        if self.data['activityID'] == 'getLoginHistory':
            responseData=LoginHistory.objects.values()

        if self.data['activityID'] == 'addService':
            try:
                categoryInstance=Category.objects.get(id=self.data['category'])
                userInstance=Users.objects.get(token=self.data['user'])
                serviceInstance= Services(thumbnail=self.data['thumbnail'],name=self.data['name'],normal_rate=self.data['normalRate'],description=self.data['description'],negotiable=bool(self.data['negotiable']),has_packages=bool(self.data['hasPackages']),url=genUrl(), category=categoryInstance,user=userInstance)
                serviceInstance.save()
                print(serviceInstance.negotiable)
                print(serviceInstance.has_packages)

                if bool(self.data['hasPackages']):
                for package in self.data['packages']:
                    # print(package['name'])
                    packageInstance=Packages(condition=package['name'], rate=package['rate'],service=serviceInstance)
                    packageInstance.save()
                    
                responseData={
                    'status':1,
                    'message':self.data['packages']
                }
            except Exception as e:
                responseData={
                    'status':0,
                    'message':'Error adding service. Please contact customer care for assistance, {}'.format(e)
                }

        if self.data['activityID'] == "getServices":
            try:
                userInstance=Users.objects.get(token=self.data['requestData']['token'])
                services=Services.objects.filter(user=userInstance, visibility=1).values('id', 'name', 'url').order_by('name')
                responseData={
                    'status':1,
                    'data':services
                }
            except Exception as e:
                responseData={
                    'status':0,
                    'message':'Error retrieving your services. Please contact customer care for assistance'
                }

        if self.data['activityID'] == 'getSpecificService':
            packagesDict={}
            try:
                service=Services.objects.get(url=self.data['requestData']['url'])
                if service.has_packages:
                    packages=Packages.objects.filter(service=service.id, visibility=1).values('id','condition', 'rate')
                    packagesDict=packages

                responseData={
                    'status':1,
                    'data':{
                        'id':service.id,
                        'thumbnail':service.thumbnail.name,
                        'name':service.name,
                        'category':service.category.name,
                        'category_id':service.category.id,
                        'normal_rate':service.normal_rate,
                        'description':service.description,
                        'negotiable':service.negotiable,
                        'has_packages':service.has_packages,
                        'packages':packagesDict
                    }
                }
            except Exception as e:
                responseData={
                    'status':0,
                    'message':'Error retrieving service details. Please try again after some time {}'.format(e)
                }

        if self.data['activityID'] == 'updateService':
            try:
                categoryInstance=Category.objects.get(id=self.data['category'])
                serviceInstance=Services.objects.get(id=self.data['id'])
                serviceInstance.name= self.data['name']
                serviceInstance.description= self.data['description']
                serviceInstance.negotiable= bool(self.data['negotiable'])
                serviceInstance.has_packages= bool(self.data['hasPackages'])
                serviceInstance.category= categoryInstance

                # update thumbnail
                if self.data['thumbnail'] != serviceInstance.thumbnail.name:
                    serviceInstance.thumbnail= self.data['thumbnail']

                serviceInstance.save()
                
                # handle packages
                # delete packages
                if len(self.data['packages']) == 0:
                    packages=Packages.objects.filter(service=serviceInstance.id)
                    if len(packages) > 0:
                        for package in packages:
                            package.visibility=0
                            package.save()

                # update existing packages
                if len(self.data['packages']) > 0:
                    for package in self.data['packages']:
                        # Insert new packages
                        if package['id'] == '':
                            packageInstance=Packages(condition=package['name'], rate=package['rate'],service=serviceInstance)
                            packageInstance.save()
                        else:
                            #update existing packages
                            packageInstance=Packages.objects.get(id=package['id'])
                            packageInstance.condition=package['name']
                            packageInstance.rate=package['rate']
                            packageInstance.save()

                responseData={
                    'status':1,
                    'message':"Service updated successfully"
                }
                
            except Packages.DoesNotExist:
                pass

            except Exception as e:
                responseData={
                    'status':0,
                    'message':'Error updating service. Please contact customer care for assistance {}'.format(e)
                }

        if self.data['activityID'] == 'deleteService':
            try:
                serviceInstance=Services.objects.get(id=self.data['requestData']['id'])
                serviceInstance.visibility=0
                serviceInstance.save()

                responseData={
                    'status':1,
                    'message':'Service deleted successfully'
                }
            except Exception as e:
                responseData={
                    'status':0,
                    'message':'Error deleting service. Please contact cutomer care fo assistance'
                }

        return responseData