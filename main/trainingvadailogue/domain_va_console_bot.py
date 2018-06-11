from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_nlu import config

logger = logging.getLogger(__name__)

def run_bot(serve_forever,configs):
    agent = Agent.load(configs["dialogue_model"], RasaNLUInterpreter(configs["nlu_model"]))

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())

    return agent

def main():
    configs = config.load("./config/training_va_config.yaml")
    run_bot(True,configs)

if __name__ == '__main__':
    main()