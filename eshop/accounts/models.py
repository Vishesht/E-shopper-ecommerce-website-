import razorpay
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from django.db import models

# Create your models here.
razor_api_key = settings.RAZORPAY_SECRET_KEY
client = razorpay.Client(auth=("<rzp_test_9rucf6UibIA2LO>", "<wGc2DKBbD4eFzIggoA7kXuBI>"))
client.set_app_details({"title" : "<Agrisolutions>", "version" : "<2.0.0>"})

class UserAcc(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    razorpay_id = models.CharField(max_length=120)

    def __unicode__(self):
        return str(self.razorpay_id)

#def get_or_create_razorpay(sender, user, *args, **kwargs):
    #try:
        #user.useracc.razorpay_id
    #except UserAcc.DoesNotExist:
        #customer = client.customer.create(
            #email = str(user.email),
        #)
        #new_user_razorpay = UserAcc.objects.create(
         #   user=user,
          #  razorpay_id = customer.id
        #)
    #except:
     #   pass

#user_logged_in.connect(get_or_create_razorpay)