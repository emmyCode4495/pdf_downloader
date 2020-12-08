from os import truncate
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    category_image = models.ImageField(upload_to='category/%Y/%m/%d',null=True, blank=True)

    @property
    def categoryURL(self):
        try:
            url = self.category_image.url
        except:
            url = ''
        return url
        
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    

    
class Book(models.Model):
    category = models.ForeignKey(Category,
                                  related_name='books',
                                  on_delete=models.CASCADE)
    book_name = models.CharField(max_length=500, db_index=True)
    slug = models.SlugField(max_length=200, db_index = True)
    book_author = models.CharField(max_length=200, db_index=True)
    book_edition = models.CharField(max_length= 10, null=True)
    file_type = models.CharField(max_length=10, null=True)
    file_size = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    published_year = models.PositiveSmallIntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=200)
    book_language = models.CharField(max_length=200)
    book_pages = models.PositiveSmallIntegerField(blank=True, null=True)
    book_isbn = models.PositiveSmallIntegerField(blank=True, null=True)
    book_image = models.ImageField(upload_to='books/%Y/%m/%d',null=True, blank=True)
    file_upload = models.FileField(upload_to='documents/%Y/%m/%d',null=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    book_summary = models.TextField(max_length=5000)
    author_profile = models.TextField(max_length=5000)

    def get_absolute_url(self):
        return reverse('book_app:books',
                       args=[
                            self.slug,self.published_year])
    @property
    def imageURL(self):
        try:
            url = self.book_image.url
        except:
            url = ''
        return url
        
    def __str__(self):
        return self.book_name
        
    class Meta:
        ordering = ('book_name',)
        index_together = (('id','slug')) 


    


