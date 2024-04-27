from django.contrib.auth.tokens import default_token_generator
from users.forms import UserLoginForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import logout as user_logout
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from dashboard.models import Test
from django.conf import settings
from django.contrib import auth
from django.urls import reverse
from .models import User

class Authentication:
    def login(request):
        if request.user.is_authenticated:
            user_id = request.user.id
            if Test.objects.filter(user_id=user_id).exists():
                        latest_test_id = Test.objects.filter(user_id=user_id).latest('test_date').id
                        return HttpResponseRedirect(reverse('dashboard:test_parameters', kwargs={'test_id': latest_test_id}))
            else:
                return redirect('dashboard:dashBoard')

        if request.method == 'POST':
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(request,username=username,password=password)
                if user:
                    auth.login(request,user)

                    if Test.objects.filter(user_id=user.id).exists():
                        latest_test_id = Test.objects.filter(user_id=user.id).latest('test_date').id
                        return HttpResponseRedirect(reverse('dashboard:test_parameters', kwargs={'test_id': latest_test_id}))

                    if request.POST.get('next',None):
                        return HttpResponseRedirect(request.POST.get('next'))

                    return HttpResponseRedirect(reverse('dashboard:dashBoard'))
        else:
            form = UserLoginForm()
        return render(request,'main/login.html',{'form': form})

    @login_required()
    def logout(request):
        user_logout(request)
        return redirect('main:index')


    def registration(request):
        if request.method == 'POST':
            form = UserRegistrationForm(data=request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.email  # Присвоюємо значення email полю username
                user.save()
                return HttpResponseRedirect(reverse('user:login'))
        else:
            form = UserRegistrationForm()
        return render(request,'main/registration.html',{'form':form})

class CustomPasswordReset(FormView):
    template_name = 'main/password_reset_form.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('user:password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(self.request, 'main/password_reset_form.html', {'error_message': 'Такого користувача не існує','user_email': email})
        
        token_generator = default_token_generator
        token = token_generator.make_token(user)
        
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        
        reset_url = self.request.build_absolute_uri(
            reverse('user:password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
        )
        
        subject = 'Відновлення пароля'
        message = render_to_string('main/password_reset_email.html', {'reset_url': reset_url})
        
        SendEmail = EmailMessage(
            subject,
            message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[email],
        )
        SendEmail.send()
        
        return super().form_valid(form)