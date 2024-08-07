from settings import *
from pydub.playback import play
import numpy as np

def effectBassBoosted(sound, boost_db=10, cutoff_freq=150):
    """
    Applies a bass boost effect to the sound.
    Returns the bass boosted version of the sound.
    """

    bass = sound.low_pass_filter(cutoff_freq)
    
    bass = bass + boost_db
    
    soundBassBoosted = sound.overlay(bass)
    
    return soundBassBoosted