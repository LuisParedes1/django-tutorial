from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect
from polls.models import Question, Choice
from django.db.models import F
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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


# question_id is "extracted" from the URL using string pattern matching
def detail(request: HttpRequest, question_id: int):
    return HttpResponse("You're looking at question %s." % question_id)


# If question does not exist, Http404 error is returned
def detail_with_error_handling(request: HttpRequest, question_id: int) -> HttpResponse | Http404:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return Http404("Question does not exist")
    
    return render(request, "polls/detail.html", {"question": question})

# It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut
def detail_with_error_handling_and_shortcut(request: HttpRequest, question_id: int) -> HttpResponse | Http404:
    question = get_object_or_404(Question, pk=question_id)
    # There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). 
    # It raises Http404 if the list is empty.
    return render(request, "polls/detail.html", {"question": question})


def results(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
