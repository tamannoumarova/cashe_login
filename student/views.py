from django.contrib.auth import authenticate, logout as _logout, login as _login
from django.contrib.auth.decorators import login_required as _login_required
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render, redirect
from django.db.models import Min, Max, Avg, Count
from django.views.decorators.cache import cache_page

from student.models import Student, Group


def login_required(func):
    return _login_required(func, login_url="login")


@login_required
@cache_page(60 * 1)
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            _login(request, user)
            return redirect('index')
        print(username, password)
    return render(request, 'login.html')


@login_required
def logout(request):
    _logout(request)
    return redirect('login')


# student_min_max_age = Student.objects.aggregate(min_age=Min('age'), max_age=Max('age'), avg_age=Avg('age'))
# print('Min age:', student_min_max_age.get('min_age'))
# print('Max age:', student_min_max_age.get('max_age'))
# print('Avarage age:', f"{student_min_max_age.get('avg_age'):.2f}")
# group_count = Group.objects.annotate(students_count=Count('students_count'),
#                                      students_min_age=Min('students_count__age'),
#                                      students_max_age=Max('students_count__age'),)
# for i in group_count:
#     print(f'Group name: {i.name}\nGroup count: {i.students_count}\nMin age: {i.students_min_age}\nMax age: {i.students_max_age}\n\n')

    # print(request.session.session_key)
    # print(request.session.items())
    # request.session['username'] = 'Jaxongir'
    # print(request.COOKIES)
    # result = render(request, 'index.html')
    # result.set_cookie('username', 'admin')
    # print(result.cookies)
    # return result