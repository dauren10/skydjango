from django.http import HttpResponse,HttpResponseRedirect
from .forms import TForm
from django.shortcuts import render
import logging

logger = logging.getLogger('django')
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            logger.info(request.POST)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TForm()

    return render(request, 'tickets/index.html', {'form': form})