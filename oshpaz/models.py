from django.db import models
from django.utils.text import slugify

class Profession(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    file = models.FileField(upload_to='certificates/')  

    def __str__(self):
        return f"Certificate {self.id}"


class Achievement(models.Model):
    image = models.ImageField(upload_to='achievements/')  

    def __str__(self):
        return f"Achievement {self.id}"
    
class Portfolio(models.Model):
    portfolio = models.FileField()




class User(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    GOOGLE = 1
    FACEBOOK = 2
    AUTH_TYPE_CHOICES = [
        (GOOGLE, 'Google'),
        (FACEBOOK, 'Facebook'),
    ]

    full_name = models.CharField(max_length=255)
    phone = models.BigIntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    birth_of_date = models.DateField()
    email = models.EmailField(unique=True, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    certificate = models.ForeignKey(Certificate, on_delete=models.SET_NULL, null=True, blank=True)
    achievement = models.ForeignKey(Achievement, on_delete=models.SET_NULL, null=True, blank=True)
    work_place = models.CharField(max_length=255, null=True, blank=True)
    auth_type = models.IntegerField(choices=AUTH_TYPE_CHOICES)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    product_name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.ZERO.value, null=True, blank=True)
    discount = models.IntegerField(default=0)
    slug = models.SlugField(null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='categories')
    
    @property
    def discount_price(self):
        if self.discount > 0 :
            return self.price * (1 - self.discount / 100)
        
        return self.price
    

    @property
    def pay_mont(self):
        return self.price / 12

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

class OrderMenu(models.Model):
    pass
    # product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='oredermenus')

class Scientist(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)
    position = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)

class HealthyLife(models.Model):
    retsepts = models.CharField(max_length=255)
    photo = models.FileField()
    categores = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='healthylifes')


class Comment(BaseModel):
    class RatingChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    message = models.TextField()
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.ZERO.value, null=True, blank=True)
    file = models.FileField(upload_to='comments/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PersonalPrescription(models.Model):
    name  = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.CharField(max_length=255)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    users_like = models.ManyToManyField(User, related_name='likes', blank=True, db_table='users_like')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='personalprescriptions' )

class Myerrors(models.Model):
    title = models.CharField(max_length=255)
    my_life = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    should_be_done = models.CharField(max_length=255)
    image = models.ImageField()
    users_like = models.ManyToManyField(User,blank=True , related_name='my_error_liked' )
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='myerrors' )

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField()
    