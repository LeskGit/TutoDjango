from django.test import TestCase
from monApp.models import Status

class StatusModelTest(TestCase):
    
    def setUp(self):
        self.status = Status.objects.create(libelleStatus="StatusPourTest")
        
    def test_status_creation(self):
        self.assertEqual(self.status.libelleStatus, "StatusPourTest")
        
    def test_string_representation(self):
        self.assertEqual(str(self.status), "StatusPourTest")

    def test_status_updating(self):
        self.status.libelleStatus = "StatusPourTestUpdated"
        self.status.save()
        
        updated_status = Status.objects.get(idStatus=self.status.idStatus)
        self.assertEqual(updated_status.libelleStatus, "StatusPourTestUpdated")
        
    def test_status_deletion(self):
        self.status.delete()
        self.assertEqual(Status.objects.count(), 0)

