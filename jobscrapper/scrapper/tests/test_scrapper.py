from django.test import TestCase

from ..scrapper import linkedin_scrapper


class ScrapperLinkedinTestCase(TestCase):
    def setUp(self):
        self.job_position = "python"

    def test_scrapper_linkedin_list_is_not_none(self):
        works = linkedin_scrapper(job_position=self.job_position)

        self.assertGreaterEqual(len(works), 1)
        self.assertEquals(type(works), type(list()))

    def test_scrapper_linkedin_position_containin_work_name(self):
        works = linkedin_scrapper(job_position=self.job_position)
        expected_work_position = "python"
        first_work = works[0]

        self.assertIsNotNone(first_work)
        self.assertIsNotNone(first_work["position"])
        self.assertIn(expected_work_position, first_work["position"].lower())

    def test_scrapper_linkedin_location_containin_location(self):
        job_location = "canada"
        works = linkedin_scrapper(
            job_position=self.job_position, job_location=job_location
        )
        expected_location = "canada"
        first_work = works[0]

        self.assertIsNotNone(first_work)
        self.assertIsNotNone(first_work["location"])
        self.assertIn(expected_location, first_work["location"].lower())

    def test_scrapper_linkedin_company_name_is_not_none(self):
        works = linkedin_scrapper(job_position=self.job_position)
        first_work = works[0]

        self.assertIsNotNone(first_work)
        self.assertIsNotNone(first_work["company"])
