from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from polls.models import Question
from django.template import loader
from django.shortcuts import render

# Using a template
def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-publication_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))

# It’s a very common idiom to load a template, fill a context and return an HttpResponse object 
# with the result of the rendered template. Django provides a shortcut
def index_using_shortcut(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

# If question does not exist, Http404 error is returned
def index_with_error_handling(request: HttpRequest) -> HttpResponse | Http404:
    try:
        question = Question.objects.get(pk=1)
    except Question.DoesNotExist:
        return Http404("Question does not exist")
    
    return render(request, "polls/detail.html", {"question": question})


# question_id is "extracted" from the URL using string pattern matching
def detail(request: HttpRequest, question_id: int):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request: HttpRequest, question_id: int):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse("You're voting on question %s." % question_id)