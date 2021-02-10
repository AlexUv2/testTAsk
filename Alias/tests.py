from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from .models import Alias, Target

class AliasTest(TestCase):
    def setUp(self):
        t = Target.objects.create(title='target1')
        a = Alias.objects.create(alias='alias1', target=t, 
        start=datetime.strptime("01/01/1970 00:00:00.000000", '%m/%d/%Y %H:%M:%S.%f'),
        end=datetime.strptime("01/01/1970 00:00:00.000000", '%m/%d/%Y %H:%M:%S.%f')
    