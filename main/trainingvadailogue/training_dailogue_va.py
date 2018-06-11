from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer,
                                   BinarySingleStateFeaturizer)
from rasa_nlu import config

logger = logging.getLogger(__name__)

def trainDialogue(configs):
    
    # featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(),
    #                                      max_history=5)

    agent = Agent(configs["domain_file"], policies=[MemoizationPolicy(max_history=5), KerasPolicy()])

    training_data = agent.load_data(configs["stories_file"])  
    agent.train(
        training_data,
        augmentation_factor = 50,
        epochs = 500,
        batch_size = 10,
        validation_split = 0.2)

    agent.persist(configs["dialogue_model"])
    return agent

def main():
    configs = config.load("./config/training_va_config.yaml")
    trainDialogue(configs)

if __name__ == '__main__':
    main()