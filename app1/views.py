from django.shortcuts import render,redirect

# Create your views here.



def custom_404(request, exception):
    # 这里的'home'是你想要重定向到的路由名称，你可以根据需要修改
    return redirect('login')

def login(request):
    return render(request, 'app1/login1.html')


def index(request):
    return render(request, 'app1/home.html')





