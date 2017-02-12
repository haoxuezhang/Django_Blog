from django.db import models
from django.core.urlresolvers import reverse
from collections import defaultdict
import datetime

# Create your models here.
class ArticleManage(models.Manager):    
    
    def archive(self):
        date_list = Article.objects.datetimes('created_time','month',order  = 'DESC')
        date_dict = defaultdict(list)
        for d in date_list:
            date_dict[d.year].append(d.month)
        return sorted(date_dict.items(),reverse = True)





class Article(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published'),
    )
    
    objects = ArticleManage()
    
    title = models.CharField('title',max_length = 70)
    body = models.TextField('body')
    created_time = models.DateTimeField('文章创建时间',auto_now_add = True)
    last_modified_time = models.DateTimeField('last_modified_time',auto_now = True)
    status = models.CharField('status',max_length = 1,choices = STATUS_CHOICES)
    abstract = models.CharField('abstract',max_length = 54,blank = True,null = True,help_text = 'you can choice fist 54 words as the abstruct')
    views = models.PositiveIntegerField('views',default = 0)
    likes= models.PositiveIntegerField('liskes',default = 0)
    topped = models.BooleanField('topped',default = False)
    category = models.ForeignKey('Category',verbose_name = 'category',null = True,on_delete = models.SET_NULL)
    tags = models.ManyToManyField('Tag',verbose_name = 'tags',blank = True)
    
    
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-last_modified_time']
        
    def get_absoulte_url(self):
        return reverse('blog:detail',kwargs={'article_id':self.pk})
        
        
class Category(models.Model):
    name = models.CharField('name',max_length = 20)
    created_time = models.DateTimeField('created_time',auto_now_add = True)
    last_modified_time = models.DateTimeField('last_modified_tiem',auto_now = True)
    
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    name = models.CharField('name',max_length = 20)
    created_time = models.DateTimeField('created_time',auto_now_add = True)
    last_modified_time = models.DateTimeField('last_modified_time',auto_now = True)
    
    def __str__(self):
        return self.name
    
    
class BlogComment(models.Model):
    user_name = models.CharField('user_name',max_length = 100)
    user_email = models.EmailField('user_email',max_length = 255)
    body = models.TextField('body')
    created_time = models.DateTimeField('created_time',auto_now_add = True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.body[:20]
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    