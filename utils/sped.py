from settings import *


def effectSpedUp(sound):
    """
    makes tjhe music faster fr
    """

    soundSpedUp = sound._spawn(
        sound.raw_data,
        overrides={"frame_rate": int(sound.frame_rate * speedUpMultiplier)},
    )
    soundSpedUp.set_frame_rate(sound.frame_rate)
    return soundSpedUp
