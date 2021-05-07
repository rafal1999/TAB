from django.db import models



class Candidates(models.Model):
    ID_candidate = models.AutoField(primary_key=True)
    Name = models.TextField(default="")
    Surname = models.TextField()
    def __str__(self): #musi być __str__ bo inaczej nie działa tylko wyświetla niapis że obiekt jest 
        return self.Name

    def __str__(self): #musi być __str__ bo inaczej nie działa tylko wyświetla niapis że obiekt jest 
        return self.Surname
