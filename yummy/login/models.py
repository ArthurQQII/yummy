from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return self.email

        
    def testuser(self, user):
        result = User.objects.get(email = user['email'])

        if result:
            return result['password']
    




    
