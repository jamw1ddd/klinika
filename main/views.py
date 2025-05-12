from django.shortcuts import render,get_object_or_404,redirect
from .models import Doctor, BlogPost
from .forms import AppointmentForm, ContactForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    doctors = Doctor.objects.all()[:4]
    blog_posts = BlogPost.objects.order_by('-sana')[:4]
    return render(request, 'index.html', {'doctors': doctors,'blog_posts': blog_posts})

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})


def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    memberships = [m.strip() for m in doctor.memberships.split(',')]
    education_list = doctor.education.splitlines()
    awards_list = doctor.awards.splitlines()

    context = {
        'doctor': doctor,
        'memberships': memberships,
        'education_list': education_list,
        'awards_list': awards_list,
    }
    return render(request, 'doctor_detail.html', context)


def services(request):
    return render(request,'services.html')

def service_detail(request):
    return render(request,'service_detail.html')

def blog(request):
    posts = BlogPost.objects.all().order_by('-sana')  # Blog postlarini sanaga ko‘ra tartiblaymiz
    popular_posts = BlogPost.objects.order_by('sana')[:3]  # Eng mashhur postlarni olish
    paginator = Paginator(posts, 4)  # Har bir sahifada 6 post
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {
        'posts': posts,
        'popular_posts': popular_posts,
        'page_obj': page_obj
    })

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)  # ID orqali postni olish
    return render(request, 'blog_detail.html', {'post': post})

def blog_search(request):
    query = request.GET.get('q', '')
    results = BlogPost.objects.filter(
        Q(sarlavha__icontains=query) | Q(matn__icontains=query)
    )
    return render(request, 'search_results.html', {
        'query': query,
        'results': results
    })

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # muvaffaqiyat sahifasi
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # muvaffaqiyat sahifasi
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def table(request):
    return render(request,'table.html')

def success(request):
    return render(request,'success.html')

def about(request):
    doctors = Doctor.objects.all()[:4]
    return render(request, 'about.html', {'doctors': doctors})

