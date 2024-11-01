from django.db import models

class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.titre

class Predications(models.Model):
    titre = models.CharField(max_length=200)
    orateur = models.CharField(max_length=100)
    date = models.DateField()
    video_url = models.URLField(blank=True, null=True)  # Lien vers la vidéo de l'enseignement, si disponible

    def __str__(self):
        return f"{self.titre} - {self.orateur}"
