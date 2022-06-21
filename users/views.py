from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    context = {}  # This is used to relay an error message to the template if wrong credentials are entered.
    if request.user.is_authenticated:
        pass
        # TODO: Redirect the user to the most suitable page here.

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:  # If the user credentials are valid.
            # Check user permissions to know where to redirect.
            login(request, user)
            # TODO: Redirect the user to the most suitable page here.
        else:
            messages.error(request, "Your username and password didn't match. Please try again.")

    return render(request, 'users/login.html', context=context)
