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
from django.http import HttpResponse  
from .userTasksGroups import UserTasksGroups
from .allTasksGroup import AllTasksGroup
from django.contrib.auth import get_user_model
from .taskArchive import TaskArchive, TaskRestore

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