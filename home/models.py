from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField('Name',blank=False, max_length=50, unique=True)

    class Meta:
        verbose_name_plural = u'Languages'
        ordering =['name']

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('Name',blank=False, max_length=50, unique=True)
    description = models.TextField('Description',blank=True)
    image=models.CharField('Image',max_length=200,blank=True,null=True)

    class Meta:
        verbose_name_plural = u'Categories'
        ordering =['name']

    def __unicode__(self):
        return self.name


class CategoryTranslate(models.Model):
    language = models.ForeignKey(Language,null=False,blank=False)
    category = models.ForeignKey(Category,null=False,blank=False)
    name = models.CharField('Name',blank=False, max_length=50)
    description = models.TextField('Description',blank=True)


class TypeOrganization(models.Model):
    name = models.CharField('Name',blank=False, max_length=50, unique=True)

    class Meta:
        verbose_name_plural = u'Types of Organization'
        ordering =['name']

    def __unicode__(self):
        return self.name

class TypeOrganizationTranslate(models.Model):
    language = models.ForeignKey(Language,null=False,blank=False)
    typeorganization = models.ForeignKey(TypeOrganization,null=False,blank=False)
    name = models.CharField('Name',blank=False, max_length=50)
  


class Service(models.Model):
    name = models.CharField('Name',blank=False, max_length=100, unique=True)
    description =models.TextField('Description',blank=True)
    category = models.ForeignKey(Category,null=False,blank=False)
    Type = models.ForeignKey(TypeOrganization,null=False,blank=False)
    web = models.CharField('Website',blank=True, null=True, max_length=100)
    phone = models.CharField('Phone Number',blank=True, null=True, max_length=50)
    address =models.CharField('Address',blank=True, null=True, max_length=100)
    city =models.CharField('City',blank=True, null=True, max_length=50)
    state =models.CharField('state',blank=True, null=True, max_length=2)
    zipcode = models.CharField('Zip Code',blank=True, null=True, max_length=5)
    contact= models.CharField('Contact Person',max_length=100,blank=True,null=True)
    contactemail = models.CharField('Contact Email',max_length=30,blank=True,null=True)
    contactnumber =models.CharField('Contact Number',max_length=30,blank=True,null=True)
    fee =models.BooleanField('Is there a fee for Service',default=False)
    ss =models.BooleanField('Do you ask for SS',default=False)
    created = models.DateTimeField('Date of created', auto_now_add=True)
    updated = models.DateTimeField('Date of Updated',auto_now=True)

    class Meta:
        verbose_name_plural = u'Services'
        ordering =['name']

    def __unicode__(self):
        return self.name


class ServiceTranslate(models.Model):
    language = models.ForeignKey(Language,null=False,blank=False)
    service = models.ForeignKey(Service,null=False,blank=False)
    description = models.TextField('Description',blank=True)


class InformationType(models.Model):
    name = models.CharField('Name',blank=False, max_length=50, unique=True)
    description = models.TextField('Description',blank=True)

    class Meta:
        verbose_name_plural = u'Types of Information'
        ordering =['name']

    def __unicode__(self):
        return self.name



class Information(models.Model):
    informationtype = models.ForeignKey(InformationType,null=False,blank=False)
    name = models.CharField('Name',blank=False, max_length=50, unique=True)
    description = models.TextField('Description',blank=True)

    class Meta:
        verbose_name_plural = u'Informations'
        ordering =['name']

    def __unicode__(self):
        return self.name

class InformationTranslate(models.Model):
    language = models.ForeignKey(Language,null=False,blank=False)
    information = models.ForeignKey(Information,null=False,blank=False)
    name = models.CharField('Name',blank=False, max_length=50)
    description = models.CharField('Description', max_length=500)


    
    








