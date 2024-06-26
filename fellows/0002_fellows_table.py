# Generated by Django 3.2.13 on 2022-06-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fellows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fellows_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('Fellow_Name', models.CharField(max_length=100, null=True)),
                ('Center_Name', models.CharField(max_length=100)),
                ('Total_Number_OoSC_and_Identified', models.IntegerField()),
                ('Total_Number_OoSC_and_Children_Enrolled', models.IntegerField()),
                ('Total_Classes_Conducted_This_Month', models.IntegerField()),
                ('Total_Hours_For_Hindi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Total_Hours_For_English', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Total_Hours_For_EVS', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Total_Hours_For_Math', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Number_Of_Students_attended_regularly', models.IntegerField()),
                ('Number_Of_Sessions_Done', models.IntegerField()),
                ('Number_Of_Meetings_On_Vision', models.IntegerField()),
                ('Number_Of_Meetings_On_Behaviour_Management', models.IntegerField()),
                ('Number_Of_Community_To_Understand_Local_Problems', models.IntegerField()),
                ('Number_Of_Community_Event_Organised', models.IntegerField()),
                ('Number_Of_Parents_Attended_Workshops', models.IntegerField()),
                ('Number_Of_Parents_Participated_In_Awareness_Drives', models.IntegerField()),
                ('Number_Of_Community_Members_Attended_Community', models.IntegerField()),
                ('Number_Of_Parents_Visited_Anubhuti_Learning_Centers', models.IntegerField()),
                ('Number_Of_Parents_Had_One_On_One_Conversations_With_fellows', models.IntegerField()),
                ('Rate_Your_Experience', models.IntegerField()),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
    ]
