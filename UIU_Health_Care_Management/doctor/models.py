from django.db import models
from Users.models import Person
from django.utils import timezone

class Prescription(models.Model):
    patient = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='patient_fk')
    doctor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='doctor_fk')
    symptoms = models.TextField(default="None")
    diagnosis = models.TextField(default="None")
    drug = models.TextField(default="None")
    # drug_remarks = models.TextField()
    test = models.TextField(default="None")
    # test_remarks = models.TextField()
    date = models.DateTimeField(default=timezone.now)


# class Drug(models.Model):
#     prescription_id = models.ForeignKey(Prescription, on_delete=models.CASCADE)
#     drug_name = models.CharField(max_length=50) # Name of the drug
#     remarks = models.CharField(max_length=50)

#     def __str__(self):
#         return self.prescription_id.patient.username+"-"+self.drug_name

# class Test(models.Model):
#     prescription_id = models.ForeignKey(Prescription, on_delete=models.CASCADE)
#     test_name = models.CharField(max_length=50) # Name of the drug
#     remarks = models.CharField(max_length=50)

#     def __str__(self):
#         return self.prescription_id.patient.username+"-"+self.test_name





# # Create your models here.
