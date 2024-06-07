# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nume = form.cleaned_data['nume']
            email = form.cleaned_data['email']
            mesaj = form.cleaned_data['mesaj']
            nr_telefon = form.cleaned_data['nr_telefon']
            
            email_message = EmailMessage(
                subject=f'Mesaj primit de la {nume}',
                body=f'Mesaj: {mesaj}\nNr telefon: {nr_telefon}',
                from_email='form-response@example.com',
                to=['test.mailtrap1234@gmail.com'],
                reply_to=[email],
            )
            email_message.send(fail_silently=False)
            
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def succes(request):
    return redirect('home')
