from homeassistant import core
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from .const import DOMAIN

CONF_LMS_SERVER_HOST = "lms_host"
CONF_LMS_SERVER_USERNAME = "lms_username"
CONF_LMS_SERVER_PASSWORD = "lms_password"

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_LMS_SERVER_HOST): cv.string,
                vol.Required(CONF_LMS_SERVER_USERNAME): cv.string,
                vol.Required(CONF_LMS_SERVER_PASSWORD): cv.string
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Set up the Squeezebox Extensions component"""
    from . import intent
    await intent.async_setup_intent(hass, config)
    return True
