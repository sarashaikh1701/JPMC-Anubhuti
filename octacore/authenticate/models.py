from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self,fullname, username,email,city,address,mobile,age,documents,qualification, password=None,password2=None):

        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=self.normalize_email(email),
            fullname=fullname,
            username=username,
            city=city,
            address=address,
            mobile=mobile,
            age=age,
            documents=documents,
            qualification=qualification
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_superuser(self, email, date_of_birth, password=None):
    #     """
    #     Creates and saves a superuser with the given email, date of
    #     birth and password.
    #     """
    #     user = self.create_user(
    #         email,
    #         password=password,
    #         date_of_birth=date_of_birth,
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user


class MyUser(AbstractBaseUser):

    CATEGORY = (
			('Atleat 1 yr of teaching experience', 'Atleast 1 yr of teaching experience'),
			('Teaching Degree(B.Ed)', 'Teaching Degree(B.Ed)'),
			) 
    username = models.CharField(max_length=20,unique=True)
    fullname = models.CharField(max_length=200,default='')
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    city = models.CharField(max_length=200)
    address = models.TextField(null=True)
    mobile = models.CharField(max_length=100)
    age = models.CharField(max_length=10,null=True)
    documents = models.FileField(null=True)
    qualification = models.CharField(max_length=250,null=True,choices=CATEGORY)
    designation = models.CharField(default='Fellow',max_length=100)





    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username,email,fullname,city,address,mobile,age,documents,qualification']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin