from django.shortcuts import render
from django.views.generic import TemplateView
import datetime

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        full_name = "john doe"
        today = datetime.datetime.today()
        products = ['Books', 'Toys', 'Computers']
        text = "Kelas ini khusus bagi pemula tanpa latar belakang dalam programming. Kelas ini akan membahas teknik-teknik programming dari awal hingga peserta dapat memahami dan menggunakan skillnya untuk membuat aplikasi berbasiskan Python. Kelas ini menggunakan Bahasa Indonesia."
        phone = "081212345678"
        return render(request, self.template_name, {'full_name':full_name, 'today':today, 'products':products, 'text':text, 'phone':phone})