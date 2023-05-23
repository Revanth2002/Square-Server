from django.db import models

'''----------Start : User Model----------'''
class User(models.Model):
    """Personal details"""
    name = models.CharField(max_length=256,null=True,blank=True)
    email = models.CharField(max_length=256,null=True,blank=True,unique=True)
    password = models.CharField(max_length=256,null=True,blank=True)
    phone = models.CharField(max_length=256,null=True,blank=True,unique=True)
    active = models.BooleanField(default=True)
    """Company details"""
    company_name = models.CharField(max_length=256,null=True,blank=True)
    company_address = models.CharField(max_length=256,null=True,blank=True)
    company_phone = models.CharField(max_length=256,null=True,blank=True)
    company_email = models.CharField(max_length=256,null=True,blank=True)
    company_website = models.CharField(max_length=256,null=True,blank=True)
    company_logo = models.CharField(max_length=256,null=True,blank=True)
    """Social details"""
    facebook = models.CharField(max_length=256,null=True,blank=True)
    twitter = models.CharField(max_length=256,null=True,blank=True)
    linkedin = models.CharField(max_length=256,null=True,blank=True)
    instagram = models.CharField(max_length=256,null=True,blank=True)
    """Other details"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)