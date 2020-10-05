from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Status
# Create your tests here.

User=get_user_model()

class StatusTestCase(TestCase):
    def setUp(self):
        user=User.objects.create(username='cfe',email='hello@cfe.com')
        user.set_password('yeahcfe')
        user.save()

    # def test_created_user(self):
    #     qs=User.objects.filter(username='cfe')
    #     self.assertEqual(qs.count(),1)

    def test_creating_status(self):
        user=User.objects.get(username='cfe')
        obj=Status.objects.create(user=user,content='Some cool new content')
        self.assertEqual(obj.id,1)
        qs=User.objects.all()
        self.assertEqual(qs.count(),1)