from django.shortcuts import render
from .forms import ProfileForm
from django.core.mail import send_mail

# Create your views here.
# def progfile_reg(request):
#     register = False
#     if request.method == 'POST':
#         profile_form = ProfileForm(data=request.POST)
#         if profile_form.is_valid():
#             user = profile_form.save()
#             user.set_password(user.password)
#             user.save()
#             subject = 'THANKS FOR REGISTER'
#             message = 'HEY ' + user.username + ' , you are now sucessfully register with us and your password is secure'
#             to = user.email
#             send_mail(
#                 subject,
#                 message,
#                 'fewfwefwe@fwfwfewfwe.com',
#                 [to],
#             )
#             register = True
#         else:
#             profile_form = ProfileForm(instance=profile_form)
#         return render(request, 'email/register_notifications.html', {'profile_form': profile_form, 'register': register})
