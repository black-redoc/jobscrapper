# views.py
from django.views import View
from django.template.response import TemplateResponse

from .scrapper import linkedin_scrapper


class ScrapperView(View):
    """
    ScrapperView manage the view with get and post requests
    """

    def get(self, request, *args, **kwargs):
        """
        Get scrapper/index template view
        """
        return TemplateResponse(request, "scrapper/index.html")

    def post(self, request, *args, **kwargs):
        """
        Post scrapper form request then return the template with the scrapped data
        """
        data_search = request._post
        works = linkedin_scrapper(
            job_position=data_search["work_name"], job_location=data_search["location"]
        )
        context = {"works": works}
        return TemplateResponse(request, "scrapper/index.html", context)
