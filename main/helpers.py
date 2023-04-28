from django.core.mail import send_mail
from account.models import User


def send_spam(new_product):
    users_email = [x.email for x in User.objects.all()]
    message = f"""
у нас появился новый продукт 
    
{new_product.title}
    
{new_product.description}
"""
    send_mail(
        subject="Новинка",
        message=message,
        from_email="a@gmail.com",
        recipient_list=users_email
    )
