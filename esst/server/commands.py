# coding=utf-8
# pylint: disable=missing-docstring


import os

from esst.commands import DCS, DISCORD
from esst.core import CTX, MAIN_LOGGER
from esst.utils.historygraph import make_history_graph

LOGGER = MAIN_LOGGER.getChild(__name__)


class SERVER:

    @staticmethod
    def reboot(force: bool = False):
        if DCS.there_are_connected_players() and not force:
            return 'there are connected players; cannot restart the server now (use "--force" to restart anyway)'

        LOGGER.warning('forcing restart with connected players')
        os.system('shutdown /r /t 30 /c "Reboot initialized by ESST"')
        return ''

    @staticmethod
    def show_cpu_usage_once():
        LOGGER.debug('show cpu usage once')
        CTX.server_show_cpu_usage_once = True

    @staticmethod
    def show_cpu_usage_once_done():
        LOGGER.debug('show cpu usage once: done')
        CTX.server_show_cpu_usage_once = False

    @staticmethod
    def show_cpu_usage_start():
        LOGGER.debug('show cpu usage: start')
        CTX.server_show_cpu_usage = True

    @staticmethod
    def show_cpu_usage_stop():
        LOGGER.debug('show cpu usage: stop')
        CTX.server_show_cpu_usage = False

    @staticmethod
    def show_graph(days, hours, minutes):

        def _callback(future):
            DISCORD.send(future.result())

        LOGGER.debug('show cpu usage: graph')
        make_history_graph(_callback, days, hours, minutes)
