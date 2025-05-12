from django.db import models


class Profession(models.Model):
    name = models.CharField("Kasb nomi", max_length=255, unique=True,null=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True,blank=True, verbose_name="Kasbi")
    experience_years = models.PositiveIntegerField()
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='doctors/')
    
    specialty = models.CharField(max_length=255)
    conditions = models.CharField(max_length=255)
    memberships = models.TextField(help_text="Har bir a'zolikni vergul bilan ajrating.")
    
    schedule_mon_tue = models.CharField(max_length=50, default="08:30 - 18:30")
    schedule_wed_thu = models.CharField(max_length=50, default="08:30 - 18:30")
    schedule_fri = models.CharField(max_length=50, default="08:30 - 18:30")
    schedule_sat = models.CharField(max_length=50, default="08:30 - 18:30")
    
    biography = models.TextField()
    education = models.TextField(help_text="Har bir ta’lim bandini yangi qatordan yozing.")
    research_interests = models.TextField()
    awards = models.TextField(help_text="Har bir mukofotni yangi qatordan yozing.")
    
    # social links
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name



class Appointment(models.Model):
    name = models.CharField("F.I.Sh", max_length=255)
    email = models.EmailField("Email")
    phone = models.CharField("Telefon raqam", max_length=20)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, verbose_name="Shifokor")
    date = models.DateField("Sana")
    message = models.TextField("Xabar", blank=True)

    def __str__(self):
        return f"{self.name} - {self.doctor} - {self.date}"
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.subject}"


class BlogPost(models.Model):
    sarlavha = models.CharField(max_length=200)
    muallif = models.CharField(max_length=100)
    sana = models.DateField(auto_now_add=True)
    matn = models.TextField()
    rasm = models.ImageField(upload_to='blog_rasmlar/', blank=True, null=True)

    def __str__(self):
        return self.sarlavha