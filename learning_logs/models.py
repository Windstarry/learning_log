from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    #on_delete必须设置
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.CharField(max_length=99999)
    date_added = models.DateTimeField(auto_now_add=True) 
    #存储用于管理模型的额外信息
    class Meta:
        verbose_name_plural = "entries"
    
    def __str__(self):
        if len(self.text)>50:
            return self.text[:50] + "..."
        else:
            return self.text