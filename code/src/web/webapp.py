"""
File containing the boilerplate pyramid server
"""

import os
import json
import traceback

from wsgiref.simple_server import make_server

from pyramid import request
from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.response import Response, FileResponse

from logics.NaturalTableauxSolver import NaturalTableauxSolver
from logics.senteces.Helper import create_expression, create_expression_representation
from logics.senteces.ParseExceptions import ParseException


def enable_cors_external_access(response):
    response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
        'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Max-Age': '1728000',
    })


def get_main_page(request):
    """
    Get the root file main page
    :param request: The request
    :return: The response containing the WebInterface
    """
    print(request)
    here = os.path.dirname(os.path.abspath(__file__))
    response = FileResponse(
        os.path.join(here, 'dist/index.html'),
        request=request,
        content_type='text/html'
    )
    return response


def get_file(request):
    """
    Function for the data sets that returns the data sets as files
    """
    print(request)
    here = os.path.dirname(os.path.abspath(__file__))
    response = FileResponse(
        os.path.join(here, f'files/{request.GET["name"]}'),
        request=request,
        content_type='application/json'
    )

    enable_cors_external_access(response)

    return response


def get_language_request(request: Request):
    """
    Handels the language parse request
    :param request: The request
    :return: The parse setnece or an exception
    """
    data = json.loads(request.body.decode("utf-8"))
    sentence = data['sentence']

    try:
        expression = create_expression(sentence)
        representation = create_expression_representation(expression)

        response_data = json.dumps(representation)
        response = Response(response_data)
        enable_cors_external_access(response)
        return response
    except Exception as err:
        traceback.print_exc()
        response = Response(json.dumps(dict(
            type=type(err).__name__,
            list="null" if type(err) is not ParseException else err.exception_list,
            error=str(err)
        )))
        response.status_int = 500
        enable_cors_external_access(response)
        return response


def get_solve_request(request: Request):
    request_data = json.loads(request.body.decode("utf-8"))
    expressions = [data['value'] for data in request_data['expressions']]
    to_be_shown = request_data['to_be_shown']

    try:
        nts = NaturalTableauxSolver(expressions, to_be_shown)
        nts.solve()

        sup = [exp.get_string_rep() for exp in nts.get_support()]
        sup.sort()

        response_data = json.dumps(dict(
            applied_rules={i: applied_rule.get_dict() for i, applied_rule in nts.get_applied_rules().items()},
            all_branches_closed=nts.tableaux_is_closed(),
            dot_graph=nts.get_dot_graph(),
            support=sup
        ))
        response = Response(response_data)
        enable_cors_external_access(response)
        return response
    except Exception as err:
        traceback.print_exc()
        response = Response(json.dumps(dict(
            type=type(err).__name__,
            list="null" if type(err) is not ParseException else err.exception_list,
            error=str(err)
        )))
        response.status_int = 500
        enable_cors_external_access(response)
        return response


def start_web_server():
    with Configurator() as config:
        config.add_route('main', '/')
        config.add_route('solve-request', '/solve-request')
        config.add_route('examples', '/examples')
        config.add_route('language-request', '/language-request')

        config.add_view(get_main_page, route_name='main')
        config.add_view(get_solve_request, route_name='solve-request')
        config.add_view(get_language_request, route_name='language-request')
        config.add_view(get_file, route_name='examples', http_cache=0)

        here = os.path.dirname(os.path.abspath(__file__))
        config.add_static_view("/", os.path.join(here, f'dist'))

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print("Go to: http://localhost:6543")
    server.serve_forever()
