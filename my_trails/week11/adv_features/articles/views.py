from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

@permission_required('articles.can_create', raise_exception=True)
def edit_post(request):
    # If the user doesn't have permission, raise a PermissionDenied exception. if has a permission anything below will be excuted
    return HttpResponse("You have permission to create a joutnal artice!")

