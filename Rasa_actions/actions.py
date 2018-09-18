# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action


class GetStatusPanel(Action):
    def name(self):
        return 'action_get_status'
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Все сервисы работают в штатном режиме')
        return[]
