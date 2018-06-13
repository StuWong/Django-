from django.db import models
'''
功能：
    1.创建表
    2.提供模型类，用于上层进行crud操作
'''
# Create your models here.
#需要继承该类，才能完成ORM
'''
#自定义管理器
    *1.更改默认查询集的查询结果
    *2.快速插入
'''    
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=0)
    def create(self,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread  = 0
        b.bcommet = 0
        b.isDelete = 0
        return b
'''
    @attention: 这里的create方法是用于快速插入的。
'''
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=0)
    class Meta():
        db_table = 'bookinfo'
    #BookInfo.objects.all()的返回值：
    def __str__(self):
        return self.btitle
    books1 = models.Manager()
    books2 = BookInfoManager()
    @classmethod
    def create(cls,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread  = 0
        b.bcommet = 0
        b.isDelete = 0
        return b

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=0)
    hcontent = models.CharField(max_length=1000) 
    isDelete = models.BooleanField(default=0)
    #引用外键，重点记忆
    hbook = models.ForeignKey(BookInfo)
    class Meta():
        db_table = 'heroinfo'
    #def __str__(self):
    #    return self.hname
'''

'''    