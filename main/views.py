from django.shortcuts import render


class Main:
    def index(request):
        return render(request,'main/index.html')


