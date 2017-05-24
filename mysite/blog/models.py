from django.db import models

class Post(models.Model): #class is a table
    #all these var on LHS are columns
    #RHS are datatype, constraints
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    
    #for metadata purpose, to get string text of title
    def __str__(self):
        return self.title
    
