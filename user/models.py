from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from datetime import timedelta,date
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email,username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username=models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Product(models.Model):
    Product_name=models.CharField(max_length=100,unique=True)
    price=models.PositiveIntegerField()
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.Product_name


class Order(models.Model):
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.CharField(max_length=100)
    address=models.CharField(max_length=120)
    option=(('delivered','delivered'),('cancel','cancel'),('intransit','intransit'),('ordered','ordered'))
    status=models.CharField(max_length=20,choices=option,default='ordered')
    phone_number=models.CharField(max_length=10)
    edd=date.today()+timedelta(days=5)
    delivery_date=models.DateField(null=True,default=edd)