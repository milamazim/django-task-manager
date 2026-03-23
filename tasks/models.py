from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Status'        
        verbose_name_plural = 'Status' # para nao colocar um S adicional como plural


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title