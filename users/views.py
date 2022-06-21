from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages


def view_logout(request):
    messages.info(request, f"You've logged out successfully. See you again!")
    logout(request)
    return redirect('login')


def view_login(request):
    """
    View used to log the user into their account.
    """
    if request.user.is_authenticated:  # Check to see if the user is already logged in.
        return redirect_user(request, request.user)

    if request.POST:  # Did somebody make a login attempt?
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:  # If the user credentials are valid.
            login(request, user)
            messages.info(request, f"Welcome back, {user.first_name}.")
            return redirect_user(request, user)  # Check user permissions and redirect.
        else:
            messages.error(request, "Your username and password didn't match. Please try again.")

    return render(request, 'users/login.html')


@login_required
def redirect_user(request, user):
    """
    Redirects the user to a page in which permission is granted for the particular user.
    """
    if user.has_perm('inventory.view_vehicle'):
        return redirect('inventory:overview')
