from django.shortcuts import render


def homeView(request):
  context ={
    "title":"home",
  }
  return render(request, 'base/home.html', context)
