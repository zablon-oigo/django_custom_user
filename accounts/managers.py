from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique 
    identifiers for authentication instead of username 
    """
    def create_user(self, email, password, **extra_fields):
        """"
        create and save a USer with the give email and password
        
        """
        if not email:
            raise ValueError("The Email must be set")
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        create and save the SuperUser with the given email and password
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)
    
    def get_full_name(self):
        full_name='%s%s'%(self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
