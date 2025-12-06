from django.db import models

# Create your models here.
class teacherinfo(models.Model):
    fullname: models.TextField(max_length=100)
    email:models.EmailField()
    studentid:models.TextField()
    department:models.TextField()
    password:models.TextField()
    confirmpassword:models.TextField()
    def ___str___(self):
        return self.fullname



