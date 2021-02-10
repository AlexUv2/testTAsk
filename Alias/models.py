from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import datetime


class Target(models.Model):   #родительская
    title = models.CharField(max_length=24, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title',)
    
    def get_absolute_url(self):
        return reverse("target")


class Alias(models.Model): #дочерняя 
    alias = models.CharField(max_length=255)
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    start = models.DateTimeField(blank=True)
    end = models.DateTimeField(blank=True)

    def __str__(self):
        return self.alias
    
    class Meta:
        ordering = ('-target',)

    def get_absolute_url(self):
        return reverse('list')

    @property
    def is_past_due(self):
        if self.end is None:
            return True
        return self.end > timezone.now()
    

def get_aliases(target, time_from="01/01/1970 00:00:00.000000", time_to="01/01/1970 00:00:00.000000"):
    '''Function for getting aliases by target name and date'''
    alias_objects = Alias.objects.all()
    required_objects = []

    time_from = datetime.strptime(time_from, '%m/%d/%Y %H:%M:%S.%f')
    time_to = datetime.strptime(time_to, '%m/%d/%Y %H:%M:%S.%f')
    target = str(target)

    for i in alias_objects:
        if target in i.target.title:
            #if (time_from >= i.start) and (time_to <= i.end):
            if (time_from >= datetime.strptime(datetime.strftime(i.start,'%m/%d/%Y %H:%M:%S.%f'), '%m/%d/%Y %H:%M:%S.%f') ) and (time_to <= datetime.strptime(datetime.strftime(i.end,'%m/%d/%Y %H:%M:%S.%f'), '%m/%d/%Y %H:%M:%S.%f')):
                required_objects.append(i) 

    return required_objects
    
