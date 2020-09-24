import json

from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db.models import CASCADE


class Comment(models.Model):
    title = models.CharField(255)
    comment = models.TextField()
    send_date = models.DateTimeField(auto_now=True)
    related_user = models.ForeignKey(User, on_delete=CASCADE)
    post = models.ForeignKey("Post", related_name="comments",
                             on_delete=CASCADE)

    def as_json(self):
        data = {
            "title": self.title,
            "comment": self.comment,
            "send_date": repr(self.send_date),
            "user": self.related_user.get_full_name(),
            }
        return json.dumps(data)


class Tags(models.Model):
    tag = models.CharField(32)

    def as_json(self):
        return json.dumps({"tag": self.tag})


class Post(models.Model):
    title = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    content = models.TextField()
    related_tags = models.CharField(max_length="255")

    def as_json(self):
        data = {
            "title": self.title,
            "published_date": repr(self.published_date),
            "is_active": self.is_active,
            "content": self.content,
            "related_tags": [k.as_json() for k in self.related_tags.all()],
            "comments": [k.as_json() for k in self.comments.all()]
            }
        return json.dumps(data)
