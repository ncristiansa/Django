# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'
