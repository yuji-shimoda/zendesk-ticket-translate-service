import os
import boto3
import boto3.session
import logging
from zendesk import update_ticket, get_description
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
TOKYO = 'ap-northeast-1'
TARGET_LANG = os.environ['TARGET_LANG']


def message(event, context):
    zendesk_id = event['detail']['ticket_event']['ticket']['id']
    description = get_description(zendesk_id)
    # TODO imprement description(text size) check logic
    # A UTF-8 text string. Each string should contain at least 20 characters
    # and must contain fewer that 5,000 bytes of UTF-8 encoded characters.
    try:
        session = boto3.session.Session()
        comprehend = session.client('comprehend', region_name=TOKYO)
        res = comprehend.detect_dominant_language(
            Text=description
        )
        lang = res['Languages'][0]['LanguageCode']
        if lang != TARGET_LANG:
            translate = session.client('translate', region_name=TOKYO)
            res = translate.translate_text(
                Text=description,
                SourceLanguageCode=lang,
                TargetLanguageCode=TARGET_LANG
            )
            update_ticket(zendesk_id, res['TranslatedText'])
    except Exception as e:
        logger.exception("message {}".format(e))
        raise
