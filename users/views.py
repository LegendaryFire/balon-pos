from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    """
    View used to log the user into their account.
    """
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
            return redirect_user(request, user)
        else:
            messages.error(request, "Your username and password didn't match. Please try again.")

    return render(request, 'users/login.html', context=context)


@login_required
def redirect_user(request, user):
    """
    Redirects the user to a page in which permission is granted for the particular user.
    """
    if user.has_perm('inventory.view_vehicle'):
        return redirect('inventory:overview')
