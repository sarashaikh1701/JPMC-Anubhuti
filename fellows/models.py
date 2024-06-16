from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    addr = models.CharField(max_length=200, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)


    def __str__(self):
        return self.name

class Fellows_table(models.Model):
    month = models.CharField(max_length=20)
    Fellow_Name = models.CharField(max_length=100,null=True)
    Center_Name = models.CharField(max_length=100)
    Total_Number_OoSC_and_Identified = models.IntegerField()
    Total_Number_OoSC_and_Children_Enrolled = models.IntegerField()
    Total_Classes_Conducted_This_Month = models.IntegerField()
    Total_Hours_For_Hindi = models.DecimalField(max_digits=5, decimal_places=2)
    Total_Hours_For_English = models.DecimalField(max_digits=5, decimal_places=2)
    Total_Hours_For_EVS = models.DecimalField(max_digits=5, decimal_places=2)
    Total_Hours_For_Math = models.DecimalField(max_digits=5, decimal_places=2)
    Number_Of_Students_attended_regularly = models.IntegerField()
    Number_Of_Sessions_Done = models.IntegerField()
    Number_Of_Meetings_On_Vision = models.IntegerField()
    Number_Of_Meetings_On_Behaviour_Management = models.IntegerField()
    Number_Of_Community_To_Understand_Local_Problems = models.IntegerField()
    Number_Of_Community_Event_Organised = models.IntegerField()
    Number_Of_Parents_Attended_Workshops = models.IntegerField()
    Number_Of_Parents_Participated_In_Awareness_Drives = models.IntegerField()
    Number_Of_Community_Members_Attended_Community = models.IntegerField()
    Number_Of_Parents_Visited_Anubhuti_Learning_Centers = models.IntegerField()
    Number_Of_Parents_Had_One_On_One_Conversations_With_fellows = models.IntegerField()
    Rate_Your_Experience = models.IntegerField()
    Location = models.CharField(max_length=100)

    def __str__(self):
        return self.Fellow_Name