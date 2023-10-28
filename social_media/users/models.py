from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    
    """
    Default custom user model for social_media.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    profile_image = models.ImageField(blank=True,null=True,upload_to="profile_images/")
    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    bio= models.CharField(max_length=128,blank=True,null=True)

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username,"pk":self.id})
        
    def get_social_media_links(self):
        return SocialMediaLink.objects.filter(user=self.user)
class UserSocialMeiaLink(models.Model):
    SOCIAL_MEIDA=(
        ('facebook','facebook'),
        ('instagram','instagram'),
        ('X','X'),
    )
    # Social Media Account
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    platform =models.CharField(max_length=28,blank=True,null=True,choices=SOCIAL_MEIDA)
    link = models.URLField(max_length=255)