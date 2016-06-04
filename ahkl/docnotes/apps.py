from __future__ import unicode_literals

from django.apps import AppConfig

from watson import search as watson


class DocnotesConfig(AppConfig):
    name = 'docnotes'
    def ready(self):
    	Patients = self.get_model("Patients")
    	watson.register(Patients, fields=("name"))



