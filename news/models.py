from django.db import models
from account.models import User


class Link(models.Model):
    title = models.CharField(max_length=40, verbose_name="عنوان")
    url = models.URLField(verbose_name="آدرس")
    description = models.TextField(max_length=120, verbose_name="توضیحات")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    like = models.ManyToManyField(User, verbose_name="پسندیدن", related_name="likes")
    dislike = models.ManyToManyField(User, verbose_name="نپسندیدن", related_name="dislikes")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد")

    class Meta():
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE, verbose_name="کاربر")
    link = models.ForeignKey(Link, related_name="comments", verbose_name="خبر", on_delete=models.CASCADE)
    text = models.TextField(max_length=60, verbose_name="متن")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد")

    class Meta():
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return "نظر " + self.user.first_name + self.user.last_name + " در " + self.link.title
