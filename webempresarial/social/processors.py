from .models import Link

def ctx_dict(request):
    ctx = {}
    try:
        links = Link.objects.all()
        for link in links:
            ctx[link.key] = link.url
    except Exception:
        pass  
    return ctx