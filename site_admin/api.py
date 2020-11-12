from consumer.models import Category
from django.utils import timezone
class API:

    def __init__(self, data):
        self.data=data

    def api(self):
        responseData={}
        if self.data["activityID"] == "addCategory":
            try:
                for category in self.data["requestData"]['categories']:
                    categoryInstance=Category(thumbnail=category['thumbnail'], name=category['name'])
                    categoryInstance.save()

                responseData={
                    "status":1,
                    "message":"Categories added successfully"
                }
            except Exception as e:
                responseData={
                    "status":0,
                    "message":"Error occured while adding categories. Please try again later {}".format(e)
                }
        if self.data["activityID"] == "getCategories":
            try:
                categories=Category.objects.filter(visibility=1).values("id","thumbnail","name")
                responseData={
                    "status":1,
                    "data":categories
                }
            except:
                responseData={
                    "status":0,
                    "message":"Error retrieving categories. Please try again later"
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