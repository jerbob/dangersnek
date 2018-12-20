"""Constants for use in the main application."""

from os import environ


API_PARAMS = {
    'key': environ.get('TOMTOM_API_KEY')
}
