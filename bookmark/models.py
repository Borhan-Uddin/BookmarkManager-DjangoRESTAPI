from django.db import models
class Folder(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

class Bookmark(models.Model):
    Name = models.CharField(max_length=200)
    url = models.URLField()
    folder_id = models.ForeignKey(Folder, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

