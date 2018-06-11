from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_nlu import config

logger = logging.getLogger(__name__)

def launchInteractiveTraining(input_channel, configs):
    nlu_interpreter = RasaNLUInterpreter(configs["nlu_model"])
    agent = Agent(configs["domain_file"], policies=[MemoizationPolicy(), KerasPolicy()], interpreter=nlu_interpreter)

    agent.train_online(configs["stories_file"],
                       input_channel=input_channel,
                       max_history=3,
                       batch_size=50,
                       validation_split=0.2,
                       epochs=50)
    return agent

def main():
    logging.basicConfig(level="INFO")
    configs = config.load("./config/training_va_config.yaml")
    launchInteractiveTraining(ConsoleInputChannel(),configs)

if __name__ == '__main__':
    main()
  