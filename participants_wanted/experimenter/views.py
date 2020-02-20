from django.shortcuts import render

def index(request):
    return render(request, 'expr/index.html')

# copied from Student
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    print(user_form)
    return render(request, 'expr/register.html', context={'user_form': user_form, 'registered': registered})

# Notify (a user has applied for study)

# See bids:
# see list of all applicants & applicants' info
# accept or decline an applicant (y/n accept bid)
