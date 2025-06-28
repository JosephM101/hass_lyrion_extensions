import logging
from homeassistant.helpers import intent
from homeassistant.core import callback
from .const import DOMAIN
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

DATA_KEY = "counting_test" # change later


async def async_setup_intents(hass):
    hass.data[DATA_KEY] = 0
    intent.async_register(hass, SqueezeboxPlayIntent())


class SqueezeboxPlayIntent(intent.IntentHandler):
    """Handle SqueezeboxPlay intents"""

    intent_type = "SqueezeboxPlayIntent"
    description = "Command one or more Squeezebox players to search for and play a song from the LMS library"

    slot_schema = {
        "songtitle": str,
        "area": str,
    }

    async def async_handle(self, intent_obj):
        """Handle the intent."""

        """
        Invocation examples:
            "Play [the song] {title} by {artist}"
            "[Play|Shuffle] songs by {artist}"
        
        Steps:
            - Check if the track exists on the LMS server. If it doesn't:
                > Respond with "{title} could not be found in your library."
                > END
            - Verify the target area. If one wasn't specified but a VA Satellite was used, use the satellite's area
            - Search for media_player entities in the target area that are associated with the LMS integration
                > If multiple players are found in a single area, group them together before playback.
            - Tell player to begin playback
            - Respond with "Okay. Playing {title} by {artist} [in the {area}]."
        """

        slots = intent_obj.slots
        song = slots["songtitle"]["value"]
        area = slots.get("area", {}).get("value")
        
        intent_obj.hass.data[DATA_KEY] += 1
        count = intent_obj.hass.data[DATA_KEY]

        response = intent_obj.create_response()
        response.async_set_speech(
            f"This intent has been invoked {count} times"
        )
        return response