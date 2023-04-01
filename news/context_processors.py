from decouple import config


def sitename_context_processor(request):
    return {'sitename': config("SITE_NAME")}