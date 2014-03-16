from elmyra.ip.access.dpma.dpmaregister import DpmaRegisterAccess
from elmyra.ip.util.render.phantomjs import render_pdf
from elmyra.ip.util.text.format import slugify
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.response import Response
from pyramid.settings import asbool
from pyramid.url import route_path
from pyramid.view import view_config

def includeme(config):
    config.add_route('ops-browser', '/ops/browser')
    config.add_route('jump-dpmaregister', '/office/dpma/register/application/{document_number}')
    config.add_route('angry-cats', '/angry-cats')


@view_config(route_name='ops-browser', renderer='elmyra.ip.access.epo:templates/ops-chooser.mako')
def opsbrowser(request):
    printmode = asbool(request.params.get('print'))
    return {'project': 'elmyra.ip.access.epo', 'printmode': printmode}

@view_config(route_name='ops-browser', request_param="pdf=true", renderer='pdf')
def opspdf(request):
    name = 'elmyra-patentsearch-' + request.params.get('query')
    filename = slugify(name, strip_equals=False, lowercase=False)
    suffix = '.pdf'
    request.response.headers['Content-Disposition'] = 'inline; filename={filename}{suffix}'.format(**locals())
    print_url = request.url.replace('pdf=true', 'print=true')
    return render_pdf(print_url)

@view_config(route_name='jump-dpmaregister')
def jump_dpmaregister(request):
    document_number = request.matchdict.get('document_number')
    redirect = request.params.get('redirect')
    if document_number:
        dra = DpmaRegisterAccess()
        url = dra.get_document_url(document_number)
        if url and redirect:
            return HTTPFound(location=url)

    return HTTPNotFound('Could not find application number "{0}" in DPMAregister'.format(document_number))


@view_config(name='ops-chooser', renderer='elmyra.ip.access.epo:templates/ops-chooser.mako')
def ops_chooser(request):
    url = route_path('ops-browser', request, _query=request.params)
    return HTTPFound(location=url)

@view_config(name='portfolio-demo', renderer='elmyra.ip.access.epo:templates/portfolio-demo.mako')
def portfolio(request):
    return {'project': 'elmyra.ip.access.epo'}

@view_config(name='angry-cats', renderer='elmyra.ip.access.epo:templates/angry-cats.mako')
def angry_cats(request):
    return {}
