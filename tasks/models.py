from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=200)
    
    def __str__(self):
        return self.status
    
    class Meta:
        verbose_name = 'Status'        
        verbose_name_plural = 'Status' # para nao colocar um S adicional como plural


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='task_status')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo