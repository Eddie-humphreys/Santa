from django.shortcuts import get_object_or_404, render

from .models import Person


def person_list(request):
    persons = Person.objects.all()
    return render(request, "presents/person_list.html", {"persons": persons})


def idea_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, "presents/idea_detail.html", {'person': person})
