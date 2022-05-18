import imp
from traceback import print_tb
from .index import Index
from .taskDetailView import TaskDetailView
from .taskForms import TaskCreate, TaskUpdate, TaskDelete
from .taskCommentForms import TaskCommentCreate, TaskCommentUpdate, TaskCommentDelete
from .taskActions import TaskAction
from .kanbanLogin import KanbanLogin
from .kanbanLogout import KanbanLogout
from .userTasks import UserTasks
from .kanbanSignUp import KanbanSignUp
from django.http import HttpResponse  ,HttpResponsePermanentRedirect
from .userTasksGroups import UserTasksGroups
from .allTasksGroup import AllTasksGroup
from django.contrib.auth import get_user_model
from .taskArchive import TaskArchive, TaskRestore
from .kanbanUsers import KanbanUsers
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User,Group

def activate(request,id):  
    User = get_user_model()  
    try:  
        print("Activate account for user with id",id)
        user = User.objects.get(pk=id)  
        print("User name",user.username)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and user.is_active == False   :  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  

def mod_group(request,name,group,param):
    print('-------------------------------------------------------')
    print(name,group,param)
    user=User.objects.get(pk=name)
    print(user.username)
    if param == 'add':
        print('Add')
        group = Group.objects.get(name=group)
        user.groups.add(group)
    else:
        print('Remove')
        group = Group.objects.get(name=group)
        user.groups.remove(group)

    user.save()

    print('-------------------------------------------------------')
    return redirect('user-users')