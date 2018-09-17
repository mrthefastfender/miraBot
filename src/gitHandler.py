import json
import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    # TODO implement
    return dispatch(event)

def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """
    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))
    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'createRepository':
        return create_repo(intent_request)
    # else if intent_name == 'createDatabase':
    #     return create_database(intent_request)


    raise Exception('Intent with name ' + intent_name + ' not supported')

def get_slots(intent_request):
    return intent_request['currentIntent']['slots']

def create_repo(intent_request):

    GitTypes = get_slots(intent_request)["GitTypes"]

    #request = requests.request('POST', 'https://api.bitbucket.org/2.0/repositories/mrthefastfender/testpython', auth=('sven_preng@live.nl','Test1234'))

    return close(intent_request['sessionAttributes'],
                 'Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'Thanks, your repo on {} is ready'.format(GitTypes)})


def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response
