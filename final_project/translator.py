#sudo python3 -m pip install --upgrade --force pip
#pip3 install --upgrade ibm-watson
#pip3 install ibm-cloud-sdk-core
#pylint: disable=unused-import,line-too-long,bare-except,import-error,invalid-name,missing-final-newline

"""This is a translator module"""


import ssl
import ibm_watson
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def englishtofrench(word):
    """This class does english to french translation"""

    url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/4b2c2a96-5e36-47ac-86ed-a14487e12837'
    apikey_lt='jhJBZOp8_NiZA5pIyX3sWUFhf83OdDTi6GQjK9cfF1o9'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    language_translator.set_disable_ssl_verification(True)
    lt = language_translator
    translation = lt.translate(text=word, model_id="en-fr").get_result()
    
    if word == " ":
        print("Please enter a word")
    else:
        pass

    return translation['translations'][0]['translation']

def frenchtoenglish(word):
    """This class does english to german translation"""
    
    url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/4b2c2a96-5e36-47ac-86ed-a14487e12837'
    apikey_lt='jhJBZOp8_NiZA5pIyX3sWUFhf83OdDTi6GQjK9cfF1o9'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    language_translator.set_disable_ssl_verification(True)
    lt = language_translator
    translation = lt.translate(text=word, model_id="fr-en").get_result()
    return translation['translations'][0]['translation']