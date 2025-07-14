from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import loader
from django.shortcuts import render

# Using a template
def index(request):
    latest_question_list = Question.objects.order_by("-publication_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))

# It’s a very common idiom to load a template, fill a context and return an HttpResponse object 
# with the result of the rendered template. Django provides a shortcut
def index_using_shortcut(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)