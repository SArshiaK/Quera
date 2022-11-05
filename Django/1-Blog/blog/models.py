from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def copy(self):
        blog = BlogPost.objects.get(pk=self.pk)
        # comments = blog.comment_set.all()
        comments = Comment.objects.filter(blog_post__id=self.pk)

        blog.pk = None
        blog.save()

        for comment in comments:
            comment.pk = None
            comment.blog_post = blog
            comment.save()
        return blog.id

    # def __str__(self):
    #     return self.pk


class Comment(models.Model):
    blog_post = models.ForeignKey(to=BlogPost, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
