from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    PRIORITIES = (
        [1, 'Low'],
        [2, 'Medium'],
        [3, 'High'],
    )
    STATUSES = (
        [True, 'Done'],
        [False, 'In Progress'],
    )
    
    title = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITIES, default=1)
    status = models.BooleanField(choices=STATUSES, default=False)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering ='status', 'deadline', '-priority'
        
    def __str__(self):
        return f"{self.deadline:%d.%m.%Y}"
        
    def get_absolute_url(self):
        return reverse('task', kwargs={'pk': self.pk})
        
        
    