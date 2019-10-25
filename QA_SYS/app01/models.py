from django.db import models

# Create your models here.

class Questions(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    detailDesc=models.CharField(max_length=300)
    answerCount=models.IntegerField()
    lastModified=models.DateField()

class Answers(models.Model):
    id=models.AutoField(primary_key=True)
    ansContent=models.CharField(max_length=300)
    ansDate=models.DateField()
    questions=models.ForeignKey(to="Questions",to_field="id",on_delete=models.CASCADE)
