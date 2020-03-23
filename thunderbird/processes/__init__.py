from .wps_say_hello import SayHello
from .wps_update_metadata import UpdateMetadata

processes = [
    SayHello(),
    UpdateMetadata(),
]
