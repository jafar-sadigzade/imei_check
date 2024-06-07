from django.db import models


class Phone(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Marka", help_text="Marka əlavə olunmalıdır!")
    model = models.CharField(max_length=50, verbose_name="Model", help_text="Model əlavə olunmalıdır!")
    imei = models.CharField(max_length=15, unique=True, verbose_name="IMEI", help_text="İmei əlavə olunmalıdır")
    note = models.TextField(blank=True, null=True, verbose_name="Əlavə məlumat", help_text="Vacib deyil!")
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Daxili olma tarixi")
    STATUS_CHOICES = [
        ('Qeydiyyatdan keçirilməyib!', 'Qeydiyyatdan keçirilməyib!'),
        ('Qeydiyyatdan keçib!', 'Qeydiyyatdan keçib!')
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Qeydiyyatdan keçirilməyib!",
                              verbose_name="Status")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.imei}"

    class Meta:
        verbose_name = "Telefon"
        verbose_name_plural = "Telefonlar"
        ordering = ["-added_date"]


class Recipient(models.Model):
    name = models.CharField(max_length=50, verbose_name="Adı", help_text="Maksimum 50 simvol")
    email = models.EmailField(verbose_name="Elektron poçt", help_text="Boş saxlanıla bilməz")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Elektron poçt alıcısı"
        verbose_name_plural = "Elektron poçt alıcıları"
