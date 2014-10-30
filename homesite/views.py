from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Template, Context


def current_datetime(request):
    now = datetime.datetime.now()
    html ="<html><body>It is now %s.<body></html>" % now
    return HttpResponse(html)

def current_datetime2(request):
    now = datetime.datetime.now()
    # fp = open('/home/congsl/tmp/homesite/homesite/templates/views/current_datetime.html')
    # t = Template(fp.read())
    # fp.close()

    # t = get_template("views/current_datetime.html")
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render_to_response("views/current_datetime.html",{'current_date':now})

def hours_ahead(request,offset):
    offset=int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
