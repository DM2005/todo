from django.shortcuts import render,redirect
from .models import Todo, Profile
def home(request):
  

    return render(request,"home.html")



def todo(request):
    completed_todo=[]
    todos= Todo.objects.filter(is_completed=False)
    
    
   

    parameters={
        "todos": todos,
        "name": "Devansh"
    }
    return render(request,"todo.html",parameters)


def add_todo(request):

    if request.method == "POST":


        task= request.POST.get("task")

        created_at= request.POST.get("created_at")

        new_todo = Todo(task=task, created_at=created_at)
        new_todo.save()
        return redirect("todo")
    return render(request, "add_todo.html")

def delete_todo(request,todo_id):

    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("todo")


   
def update_todo(request,todo_id):

    todo=Todo.objects.get(id=todo_id)

    if request.method == "POST":
        user_task=request.POST.get("task")
        created_at=request.POST.get("created_at")

        todo.task=user_task
        todo.created_at=created_at
        
        todo.save()
        return redirect("todo")

    parameters={
        'todo':todo
    }
    return render(request, "update_todo.html", parameters)



    
def mark_complete(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    
    todo.is_completed = True
    todo.save()
    
    return redirect("todo")

# ================================== UPLOAD PROFILE ===============================

def upload_profile(request):
    
    if request.method == "POST":
        profile_pic = request.FILES["profile_pic"]
        
        new_profile = Profile(
            title="demo title",
            profile_pic = profile_pic
            )
        
        new_profile.save()
        
        return redirect("todo")
    
    return render(request, "upload_profile.html")
# Create your views here.


