from django.db import models

# Create your models here.
class Topic(models.Model):
    """ O que foi feito nesse site"""
    text=models.CharField(max_length=200)
    data_added=models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        """Devolve uma representacao em string do modelo"""
        return self.text

class Entry(models.Model):
    """Algo especifico aprendido sobre o assunto"""
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    text=models.TextField()
    data_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='entries'
    
    def _str_(self):
        """devolve uma representacao em string do modelo"""
        return self.text[:50] +'...'
