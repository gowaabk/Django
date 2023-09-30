from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    response = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
                        <title>Django Project</title>
                    </head>
                    <body>
                        <H1>Django project</H1>
                        <p style="color:red";>Первый проект на джанго.</p>
                        <a href="/about/">О нас</a>
                    </body>
                    </html>"""
    logger.info("Start main page")
    return HttpResponse(response)


def about(request):
    response = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
                        <title>Django Project</title>
                    </head>
                    <body>
                        <H1>О себе</H1>
                        <p style="color:red">Ищу зарплату, работу не предлагать.</p>
                        <a href="/">Главная</a>
                    </body>
                    </html>"""
    logger.info("start about us")
    return HttpResponse(response)
