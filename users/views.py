import re
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import Group

from carts.models import Cart
from orders.models import Order, OrderItem
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


users_roles = {
    'customer': 'покупатель',
    'seller': 'продавец',
    'staff_warehouse': 'сотрудник склада',
    'staff_delivery': 'сотрудник доставки',}


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            requested_role = request.POST.get('role')  # customer, seller, staff_warehouse или staff_delivery
            
            user = auth.authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Неверный логин или пароль")
                print("Неверный логин или пароль")
            else:
                old_session_key = request.session.session_key
                if old_session_key:
                    Cart.objects.filter(session_key=old_session_key).update(user=user)

                # 1) Суперпользователь
                if user.is_superuser:
                    auth.login(request, user)
                    messages.success(request, f"{username}, вы вошли как { users_roles[requested_role] }")
                    print(f"{username}, вы вошли как { users_roles[requested_role] }")
                    return HttpResponseRedirect(reverse('admin:index'))  # или ваш админский дашбоард
                
                # 2) Обычный пользователь — проверяем роль
                if not requested_role or not user.groups.filter(name=requested_role).exists():
                    messages.error(request, "У вас нет прав для входа под этой ролью")
                    print("У вас нет прав для входа под этой ролью")
                else:
                    messages.success(request, f"{username}, вы вошли как { users_roles[requested_role] }")
                    print(f"{username}, вы вошли как { users_roles[requested_role] }")
                    auth.login(request, user)

                    # messages.success(request, f"{username}, вы вошли в аккаунт как { users_roles[requested_role] }")

                    redirect_page = request.POST.get('next', None)
                    if redirect_page and redirect_page != reverse('user:logout'):
                        return HttpResponseRedirect(redirect_page)
                    
                    return HttpResponseRedirect(reverse('main:index'))
            
                # # Редиректим в «свой» раздел
                # if requested_role == 'customer':
                #     return redirect('main:index')
                # elif requested_role == 'seller':
                #     return redirect('seller:dashboard')
                # elif requested_role == 'staff_warehouse':
                #     return redirect('warehouse:dashboard')
                # elif requested_role == 'staff_delivery':
                #     return redirect('delivery:dashboard')
                # else:
                #     return redirect('main:index')
    else:
        form = UserLoginForm()

    context = {
        'title': 'МО-ШОП — Авторизация',
        'form': form,
    }

    return render(request, 'users/login.html', context)


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
            
#             session_key = request.session.session_key

#             if user:
#                 auth.login(request, user)
#                 messages.success(request, f"{username}, вы вошли в аккаунт")
                
#                 if session_key:
#                     Cart.objects.filter(session_key=session_key).update(user=user)

#                 redirect_page = request.POST.get('next', None)
#                 if redirect_page and redirect_page != reverse('user:logout'):
#                     return HttpResponseRedirect(redirect_page)

#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserLoginForm()

#     context = {
#         'title': 'МО-ШОП — Авторизация',
#         'form': form,
#     }

#     return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            # Назначаем группу по выбору в <select name="role">
            # Значения селекта: 'customer', 'seller', 'staff_warehouse', 'staff_delivery'
            selected_role = request.POST.get('role')
            # Группы в БД должны иметь точно такие же имена
            if selected_role:
                try:
                    grp = Group.objects.get(name=selected_role)
                    user.groups.add(grp)
                except Group.DoesNotExist:
                    # Если группа не найдена — можно залогировать или проигнорировать
                    pass

            messages.success(request,
                             f"{user.username}, вы успешно зарегистрировались и вошли в аккаунт как { users_roles[selected_role] }")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'МО-ШОП — Регистрация',
        'form': form,
    }

    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Профиль успешно обновлён")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)


    # Можно вынести сам запрос в отдельный метод этого класса контроллера
    orders = Order.objects.filter(user=request.user).prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related("product"),
            )
        ).order_by("-id")


    context = {
        'title': 'МО-ШОП — Личный кабинет',
        'form': form,
        'orders': orders,
    }

    return render(request, 'users/profile.html', context)


def users_cart(request):
    return render(request, 'users/users_cart.html')


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

