from django.db import models

class Questionnaire(models.Model):
    id = models.AutoField(primary_key=True, db_column='que_id')
    nom = models.CharField(max_length=255, db_column='que_nom')
    quartier = models.CharField(max_length=255, db_column='que_quartier')
    quartier_futur = models.CharField(max_length=255, null=True, blank=True, db_column='que_quartier_futur')
    org_ville_demain = models.TextField(max_length=255, db_column='que_org_ville_demain')
    hum_ville_demain = models.CharField(max_length=255, blank=True, null=True, db_column='que_hum_ville_demain')

    class Meta:
        verbose_name = "Questionnaire"
        verbose_name_plural = "Questionnaire"
        ordering = ['id']

    def __str__(self):
        return "{0}".format(self.nom)



class Questionnaire_affiche(models.Model):
    id = models.AutoField(primary_key=True, db_column='que_id')
    quartier_a = models.CharField(max_length=255, db_column='que_quartier_a')
    quartier_futur_a = models.CharField(max_length=255, null=True, blank=True, db_column='que_quartier_futur_a')
    org_ville_demain_a = models.TextField(max_length=255, db_column='que_org_ville_demain_a')
    hum_ville_demain_a = models.CharField(max_length=255, blank=True, null=True, db_column='que_hum_ville_demain_a')

    class Meta:
        verbose_name = "Questionnaire_affiche"
        verbose_name_plural = "Questionnaires_affiches"
        ordering = ['id']

    def __str__(self):
        return "{0}".format(self.id)
