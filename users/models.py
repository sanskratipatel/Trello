from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
# Create your models here.

class Role(models.Model) : 
    ADMIN  = "ADMIN" 
    MANAGER = "MANAGER" 
    USER  = "USER" 
    ROLE_CHOICES =[ 
        (ADMIN , "Admin") , 
        (MANAGER , "Manager") , 
        (USER , "User") ,
    ] 

    name = models.CharField(max_length=20 , choices=ROLE_CHOICES , unique=True) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name 


class UserManager(BaseUserManager) : 
    def create_user(self, email , password =None , **extra_fields) : 
        if not email : 
            raise ValueError("Email is Required" )
        email = self.normalize_email(email) 
        if "role" not in extra_fields : 
            extra_fields["role"] = Role.objects.get( 
                name =Role.USER
            ) 
        user = self.model( 
            email =email, 
            **extra_fields
        ) 
        user.set_password(password) 
        user.save(using=self._db) 
        return user 

    
    def create_superuser(self,email,password=None , **extrafields) : 
        extrafields.setdefault("is_staff" , True) 
        extrafields.setdefault("is_superuser" , True)
        return self.create_user( 
            email=email, 
            password= password , 
            **extrafields
        )
    

class User(AbstractBaseUser, PermissionsMixin) : 
    name = models.CharField(max_length=100 ) 
    email = models.EmailField(unique=True) 
    role= models.ForeignKey(Role , on_delete=models.PROTECT ,related_name="users" ,null=False ,blank=False)
    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at =models.DateTimeField(auto_now=True) 
    objects = UserManager() 
    USERNAME_FIELD ='email' 
    REQUIRED_FIELDS=['name'] 
    def __str__(self):
        return self.email
    