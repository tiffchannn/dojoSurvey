from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")


# when user goes to /result, will display all info from submitted form
def process(request):
    print("*"*60)
    print("Got POST Info -----")
    print("POST Request: ", request.POST)
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_from = request.POST['language']
    comment_from_form = request.POST['comment']
    context = {
      "name_on_template": name_from_form,
      "location_on_template": location_from_form,
      "language_on_template": language_from_from,
      "comment_on_template": comment_from_form
    }
    return render(request, "show.html", context)


def success(request):
  print("Success!")
  return render(request, "show.html")


