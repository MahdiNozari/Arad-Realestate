from  django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, email, phone, password):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name,phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password=None):
        from .models import Agent
        agent = Agent.objects.create(
            email=email,
            name=name,
            phone=phone,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        agent.set_password(password)
        agent.save(using=self._db)
        return agent


