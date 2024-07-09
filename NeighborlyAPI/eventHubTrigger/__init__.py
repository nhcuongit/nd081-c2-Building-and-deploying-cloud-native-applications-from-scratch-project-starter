import json
import logging
import azure.functions as func


def main(event: func.EventGridEvent):

    logging.info('Starting Event Grid Trigger...')
    logging.info(f'Function triggered to process a message: {event.id}')
    logging.info(f'  EventTime = {event.event_time}')

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    logging.info(f'Python EventGrid trigger processed an event: {result}')



