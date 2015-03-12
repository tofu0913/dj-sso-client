from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    context = RequestContext(request)
    # try:
    #     u = request.user
    #     # print u, u.last_name,
    #     # import cPickle
    #     # ex = cPickle.loads(str(u.extras))
    #     # print ex
    # except:
    #     import traceback
    #     traceback.print_exc()
    #     pass
    return render_to_response("index.html", {"req": request}, context_instance=context)
