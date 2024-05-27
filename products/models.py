from django.db import models

class ProductColorModel(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=7)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'colour'
        verbose_name_plural = 'colours'

class ProductManufactureModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'manufacture'
        verbose_name_plural = 'manufactures'

class ProductSizeModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'

class ProductTagModel(models.Model):
    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=128)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class ProductModel(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=7, decimal_places = 2)
    description = models.TextField()
    short_info = models.TextField()
    discount = models.IntegerField(default=0)
    count = models.IntegerField()
    sku = models.CharField(max_length=10, unique=True, null=True)

    colors = models.ManyToManyField(ProductColorModel, related_name='products')
    manufacture = models.ForeignKey(ProductManufactureModel, on_delete=models.CASCADE, related_name='products')
    size = models.ManyToManyField(ProductSizeModel, related_name='products')
    tags = models.ManyToManyField(ProductTagModel, related_name='tags')
    categories = models.ManyToManyField(ProductCategoryModel, related_name='products')

    image = models.ImageField(upload_to='products/')
    image1 = models.ImageField(upload_to='product/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.discount * self.price / 100 

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'





