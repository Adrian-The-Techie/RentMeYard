from consumer.models import Category, Users, Services
from django.utils import timezone
from consumer.modules.api_general import determineHost, genDateTimeString


class API:

    def __init__(self, data):
        self.data = data

    def api(self):
        responseData = {}
        if self.data["activityID"] == "saveCategory":
            try:
                action = ""
                # for category in self.data['categories']:
                if self.data['id'] == None:
                    action = "added"
                    categoryInstance = Category(
                        thumbnail=self.data['thumbnail'], name=self.data['name'])
                    categoryInstance.save()
                else:
                    action = "updated"
                    categoryInstance = Category.objects.get(id=self.data['id'])
                    categoryInstance.name = self.data['name']
                    categoryInstance.date_updated = timezone.now()
                    categoryInstance.save()

                responseData = {
                    "status": 1,
                    "message": "Category {} successfully".format(action)
                }
            except Exception as e:
                responseData = {
                    "status": 0,
                    "message": "Error occured while ategory. Please try again later {}".format(e)
                }
        if self.data["activityID"] == "getCategories":
            try:
                categories = Category.objects.filter(visibility=1).values(
                    "id", "thumbnail", "name", "url").order_by("name")
                for category in categories:
                    category['thumbnail'] = '{}/media/{}'.format(
                        determineHost(), category['thumbnail'])

                responseData = {
                    "status": 1,
                    "data": categories
                }
            except Exception as e:
                responseData = {
                    "status": 0,
                    "message": "Error retrieving categories. Please try again later {}".format(e)
                }
        if self.data["activityID"] == "getCategory":
            # try:
            category = Category.objects.filter(
                url=self.data["data"]['url']).values()[0]

            category['thumbnail'] = '{}/media/{}'.format(
                determineHost(), category['thumbnail'])
            category['date_added'] = genDateTimeString(category['date_added'])
            category['noOfServices'] = Services.objects.filter(
                url='url').count()

            responseData = {
                "status": 1,
                "data": category
            }
            # except Exception as e:
            #     responseData = {
            #         "status": 0,
            #         "message": "Error retrieving category. Please try again later {}".format(e)
            #     }

        if self.data["activityID"] == "updateCategory":
            try:
                categoryInstance = Category.objects.get(
                    id=self.data["data"]["id"])
                categoryInstance.name = self.data["data"]["name"]
                categoryInstance.date_updated = timezone.now()

                categoryInstance.save()

                responseData = {
                    "status": 1,
                    "message": "Category updated successfully"
                }
            except:
                responseData = {
                    "status": 0,
                    "message": "Error updating category"
                }

        if self.data["activityID"] == "deleteCategory":
            try:
                categoryInstance = Category.objects.get(
                    id=self.data["data"]["id"])
                categoryInstance.visibility = 0

                categoryInstance.save()

                responseData = {
                    "status": 1,
                    "message": "Category deleted successfully"
                }
            except:
                responseData = {
                    "status": 0,
                    "message": "Error deleting category"
                }
        if self.data['activityID'] == "getUsers":
            try:
                users = Users.objects.filter(visibility=1, is_staff=False).values(
                    'id', 'full_names', 'date_joined', 'url')
                for user in users:
                    user['date_joined'] = genDateTimeString(
                        user['date_joined'])

                responseData = {
                    "status": 1,
                    "data": users
                }
            except Exception as e:
                responseData = {
                    "status": 0,
                    "data": None,
                    "message": "Error getting users. Please try again later {}".format(e)
                }
        if self.data['activityID'] == "getUser":
            try:
                user = Users.objects.filter(url=self.data['data']['url']).values(
                    'id', 'full_names', 'phone', 'email', 'date_joined', 'flagged', 'approved')
                user[0]['date_joined'] = genDateTimeString(
                    user[0]['date_joined'])
                print(user[0]['date_joined'])
                services = Services.objects.filter(user=user[0]['id']).values()
                for service in services:
                    service['date_added'] = genDateTimeString(
                        service['date_added'])

                responseData = {
                    "status": 1,
                    "services": services,
                    "info": user[0]
                }
            except Exception as e:
                responseData = {
                    "status": 0,
                    "data": None,
                    "message": "Error getting service. Please try again later {}".format(e)
                }
        if self.data['activityID'] == "flagUnflag":
            try:
                user = Users.objects.get(url=self.data['data']['url'])
                user.flagged = self.data['data']['flag']
                user.save()
                services = Services.objects.filter(user=user.id)
                for service in services:
                    service.flagged = self.data['data']['flag']
                    service.save()

                responseData = {
                    "status": 1,
                    "message": "User flagged successully" if self.data['data']['flag'] == True else "User unflagged successfully",
                }
            except Exception as e:
                responseData = {
                    "status": 0,
                    "message": "Error occurred. Please try again later {}".format(e)
                }
        if self.data['activityID'] == "approve":
            try:
                user = Users.objects.get(url=self.data['data']['url'])
                user.approved = True
                user.save()
                services = Services.objects.filter(user=user.id)
                for service in services:
                    service.approved = True
                    service.save()

                responseData = {
                    "status": 1,
                    "message": "{} approved".format(user.full_names),
                }
            except Exception as e:
                responseData = {
                    "status": 0,
                    "message": "Error occurred. Please try again later {}".format(e)
                }

        return responseData
