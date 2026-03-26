from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import ReadingSession, Note
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404



def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request, 'register.html')


# def user_login(request):
#     if request.method == 'POST':
#         user = authenticate(
#             username=request.POST['username'],
#             password=request.POST['password']
#         )
#         if user:
#             login(request, user)
#             return redirect('dashboard')
#     return render(request, 'login.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    sessions = ReadingSession.objects.filter(user=request.user)
    notes = Note.objects.filter(session__user=request.user)

    total = sessions.count()
    completed = sessions.filter(completed=True).count()

    return render(request, 'dashboard.html', {
        'sessions': sessions,
        'notes': notes,
        'total': total,
        'completed': completed
    })


@login_required
def start_session(request):
    if request.method == 'POST':
        session = ReadingSession.objects.create(
            user=request.user,
            book_title=request.POST['book'],
            duration=request.POST['duration'],
            break_time=request.POST['break']
        )

        # Email Notification
        send_mail(
            'Reading Session Started',
            f'You started reading {session.book_title}',
            'your_email@gmail.com',
            [request.user.email],
            fail_silently=True
        )

        return redirect('dashboard')

    return render(request, 'start_session.html')


@login_required
def add_note(request, session_id):
    if request.method == 'POST':
        Note.objects.create(
            session_id=session_id,
            content=request.POST['content']
        )
    return redirect('dashboard')


@login_required
def delete_note(request, note_id):
    if request.method == "POST":
        note = get_object_or_404(Note, id=note_id)
        note.delete()
    return redirect('dashboard')