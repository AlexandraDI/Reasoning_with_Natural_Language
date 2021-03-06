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

from logics.DefeasibleTableauxSolver import DefeasibleTableauxSolver
from logics.senteces.Helper import create_expression, create_expression_representation, expressions_to_strings, \
    expressions_to_strings_depth_2
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
    reasoning_method = request_data['reasoning_method']

    try:
        solver = DefeasibleTableauxSolver(expressions, to_be_shown, reason_by_cases=True if reasoning_method == "reasoningbycases" else False)
        solver.solve()

        supports = [[exp.get_string_rep(True) for exp in items] for items in solver.get_all_supports()]
        tableaux_closed = [tableau.all_branches_closed for tableau in solver.get_all_tableaus()]

        defeated_defeasible_expressions = expressions_to_strings(solver.get_defeated_defeasible_expressions())
        contradiction_information = expressions_to_strings_depth_2(solver.get_contradiction_information())
        contradicting_graph = solver.contradicting_graph()
        is_contradiction_in_information = solver.is_contradiction_in_information()

        response_data = json.dumps(dict(
            applied_rules=[{i: applied_rule.get_dict() for i, applied_rule in item.items()} for item in solver.get_applied_rules()],
            all_branches_closed=tableaux_closed,
            dot_graphs=solver.get_dot_graph(),
            supports=supports,
            defeated_defeasible_expressions=defeated_defeasible_expressions,
            contradiction_information=contradiction_information,
            contradicting_graph=contradicting_graph,
            is_contradiction_in_information=is_contradiction_in_information,
            is_contradiction_resolved = solver.is_contradiction_resolved()
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
