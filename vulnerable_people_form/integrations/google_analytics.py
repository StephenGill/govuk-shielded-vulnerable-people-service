import requests
import sentry_sdk
from flask import current_app


def track_event(category, action, label=None, value=0):
    data = {
        "v": "1",  # API Version.
        "tid": current_app.config["GA_TRACKING_ID"],  # Tracking ID / Property ID.
        # Anonymous Client Identifier. Ideally, this should be a UUID that
        # is associated with particular user, device, or browser instance.
        "cid": "555",
        "t": "event",  # Event hit type.
        "ec": category,  # Event category.
        "ea": action,  # Event action.
        "el": label,  # Event label.
        "ev": value,  # Event value, must be an integer
        "ua": "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    }
    response = requests.post("https://www.google-analytics.com/collect", data=data)

    # If the request fails, this will raise a RequestException. Depending
    # on your application's needs, this may be a non-error and can be caught
    # by the caller.
    response.raise_for_status()


def track_nhs_userinfo_and_form_answers_differs():
    try:
        track_event("NHS info retrieved via oidc and form differs", "registration")
    except Exception as e:
        sentry_sdk.capture_exception(e)


def track_nhs_number_and_form_value_differs():
    try:
        track_event("NHS number retrieved via oidc and that in form differs", "registration")
    except Exception as e:
        sentry_sdk.capture_exception(e)
