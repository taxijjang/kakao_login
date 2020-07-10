from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html',{})

def oauth(request):
    code = request.GET['code']
    print('code = ' + str(code))

    return redirect('index')

def kakao_login(request):
    # GET /oauth/authorize?client_id={app_key}&redirect_uri={redirect_uri}&response_type=code HTTP/1.1
    # Host: kauth.kakao.com

    host = "https://kauth.kakao.com"
    login_request_uri = host+"/oauth/authorize?"

    client_id = 'be8d497f71f0e2427a73ffe6a8b93b9d'
    redirect_uri = 'http://127.0.0.1:8000/oauth'


    login_request_uri += 'client_id=' + client_id
    login_request_uri += '&redirect_uri=' + redirect_uri
    login_request_uri += '&response_type=code'

    return redirect(login_request_uri)