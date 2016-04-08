from django.contrib.auth.decorator import login_required
from django.http import Http404
from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect

from collection.forms import ThingForm
from collection.models import Thing



def index(request):
    things = Thing.objects.all()
    return render(request, 
                    'index.html', {
                    'things': things,
                    })


def thing_detail(request, slug):
    thing = Thing.objects.get(slug=slug)
    return render(request, 'things/thing_detail.html',{
        'thing': thing,
        })


@login_required
def edit_thing(request, slug):
    thing = Thing.objects.get(slug=slug)

    # make sure the logged in user is the owner of the thing
    if thing.user != request.user:
        raise Http404

    form_class = ThingForm

    # if we're coming to this view from a submitted form"
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=thing)

    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
        })


def create_thing(request):
    form_class = ThingForm
    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but do not save yet
            thing = form.save(commit=False)
            # set the additional details
            thing.user = request.user
            thing.slug = slugify(thing.name)
            # save the object and redirect to our newly created thing
            thing.save()
            return redirect('thing_detail', slug=thing.slug)
    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'things/create_thing.html', {
        'form': form,
    })
