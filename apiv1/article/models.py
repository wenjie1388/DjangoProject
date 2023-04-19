from django.db import models

from users.models import AnyUser
from utils.utils import get_RandomString

def article_img_path(instance, filename):
    return 'article/{0}/{1}{2}'.format(instance.author,get_RandomString(24), filename)




# 文章一级分类
class Nav1(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
      )

    class Meta:
        db_table = 'nav1'
        ordering = ('id',)
        verbose_name = 'nav1'
        verbose_name_plural = 'nav1s'

    def __str__(self):
        return self.name

# 文章二级分类
class Nav2(models.Model):
    name = models.CharField(
        max_length=100,
      )
    nav1 = models.ForeignKey(
        Nav1,
        on_delete=models.CASCADE,
        to_field='name',
      )

    class Meta:
        db_table = 'nav2'
        ordering = ('id',)
        verbose_name = 'nav2'
        verbose_name_plural = 'nav2s'

    def __str__(self):
        return f'{self.Nav1}_{self.name}'


''' 阅读量 '''
class Pageviews(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name


''' 
#文章标签
class Tag(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name



#推荐位
class Tui(models.Model):
    name = models.CharField('推荐位',max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#Banner
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


#友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址',max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'admin'
        ordering = ('id',)
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'



        '''


#文章
class Article(models.Model):
    '''
    title:标题
    abstract:摘要
    img:封面
    body:内容
    author:作者
    create_date:创建日期

    '''
    title = models.CharField(max_length=64)
    abstract = models.TextField(max_length=128)
    img = models.ImageField(upload_to=article_img_path,default='article/default/default.png')
    body = models.TextField()
    author = models.ForeignKey(AnyUser, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField('修改时间', auto_now=True)
    category1 = models.ManyToManyField(Nav1)
    category2 = models.ManyToManyField(Nav2)
    #使用外键关联分类表与分类是一对多关系
    # tags = models.ManyToManyField(Tag, blank=True)
    #使用外键关联标签表与标签是多对多关系
    # views = models.PositiveIntegerField('阅读量', default=0)
    # tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)

    class Meta:
        db_table = 'article'
        ordering = ('author','create_date')
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __str__(self):
        return f'{self.id}:{self.title}:{self.user}'

class article_info(models.Model):
    '''
    id
    封面
    标题
    摘要
    标签
    '''
    pass