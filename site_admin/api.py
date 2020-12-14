from consumer.models import Category
from django.utils import timezone
from consumer.modules.api_general import determineHost
class API:

    def __init__(self, data):
        self.data=data

    def api(self):
        responseData={}
        if self.data["activityID"] == "addCategory":
            try:
                # for category in self.data['categories']:
                categoryInstance=Category(thumbnail=self.data['thumbnail'], name=self.data['name'])
                categoryInstance.save()

                responseData={
                    "status":1,
                    "message":"Category added successfully"
                }
            except Exception as e:
                responseData={
                    "status":0,
                    "message":"Error occured while adding categories. Please try again later {}".format(e)
                }
        if self.data["activityID"] == "getCategories":
            try:
                categories=Category.objects.filter(visibility=1).values("id","thumbnail","name", "url").order_by("name")
                for category in categories:   
                    category['thumbnail']='{}/media/{}'.format(determineHost(), category['thumbnail'])

                responseData={
                    "status":1,
                    "data":categories
                }
            except Exception as e:
                responseData={
                    "status":0,
                    "message":"Error retrieving categories. Please try again later {}".format(e)
                }

        if self.data["activityID"] == "updateCategory":
            try:
                categoryInstance=Category.objects.get(id=self.data["data"]["id"])
                categoryInstance.name=self.data["data"]["name"]
                categoryInstance.date_updated=timezone.now()

                categoryInstance.save()

                responseData={
                    "status":1,
                    "message":"Category updated successfully"
                }
            except:
                responseData={
                    "status":0,
                    "message":"Error updating category"
                }

        if self.data["activityID"] == "deleteCategory":
            try:
                categoryInstance=Category.objects.get(id=self.data["data"]["id"])
                categoryInstance.visibility=0

                categoryInstance.save()

                responseData={
                    "status":1,
                    "message":"Category deleted successfully"
                }
            except:
                responseData={
                    "status":0,
                    "message":"Error deleting category"
                }
            

        return responseData