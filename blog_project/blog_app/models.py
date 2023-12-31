from django.db import models

# from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField("date created", auto_now_add=True)
    views = models.IntegerField(default=0)  # visitcount
    topic = models.CharField(max_length=100)  # 주제 필드
    author = models.CharField(max_length=100, null=True, blank=True)  # 작성자 필드
    isDone = models.CharField(max_length=1, default='Y')

    def __str__(self):
        return self.title

    def increment_visit_count(self):
        self.visit_count += 1
        self.save()

    @property
    def view_count(self):
        return self.visit_count

    def check_url(self, *args, **kwargs):
        if "media/uploads/" in self.content and "/media/uploads/" not in self.content:
            self.content = self.content.replace("media/uploads/", "/media/uploads/")
            # 'media/uploads/' 문자열을 '/media/uploads/'로 교체하여 URL 형식을 수정후 저장.
        super().save(*args, **kwargs)


class admin_info(models.Model):
    information = models.CharField(max_length=200)
