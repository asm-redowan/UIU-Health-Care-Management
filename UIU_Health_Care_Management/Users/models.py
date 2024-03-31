from django.db import models
from django.utils import timezone


class Person(models.Model):
    class UserType(models.TextChoices):
        PATIENT = 'Patient', 'Patient'
        DOCTOR = 'Doctor', 'Doctor'
        

    class Dpartments(models.TextChoices):
        CSE = 'CSE', 'Computer Science & Engineering'
        EEE = 'EEE', 'Electrial & Electronics Engineering'
        CE = 'CE', 'Civil  Engineering'
        DS = 'DS', 'Data Science and Analytics'
        AD = 'AD', 'Admin'

    class Gender(models.TextChoices):
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'

    username = models.CharField(max_length=100, unique=True, primary_key=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True,null=True)
    userprofileimage = models.ImageField(upload_to="profile")
    dob = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=4, choices=Dpartments.choices)
    usertype  = models.CharField(max_length=7, choices=UserType.choices)
    gender = models.CharField(max_length=7, choices=Gender.choices)
    
    
    def __str__(self):
        return self.username+": "+self.first_name+" "+self.last_name
    


class Appointment(models.Model):

    TIME_SLOT = {
        "slot1": "9AM -11AM",
        "slot2": "11AM-1PM",
        "slot3": "1PM-5PM"
    }

    
    patient = models.ForeignKey(Person, on_delete=models.CASCADE, primary_key=True, related_name='patient_appointments')
    # doctor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='doctor_appointments')
    appointment_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)  # True if the appointment is confirmed
    slot = models.CharField(max_length=5, choices=TIME_SLOT)
    problem = models.CharField(max_length=250, null=True)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['patient', 'doctor'], name='unique_appointment')
    #     ]




