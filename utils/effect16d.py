import numpy as np
from scipy.signal import resample

def effect16d(sound, sample_rate=44100, width=1.0, depth=1.0):
    """
    makes the music go woooooooo

    Parameters:
    sound (AudioSegment): The input audio
    sample_rate (int): The sample rate of the input audio (default: 44100)
    width (float): The width of the 16D effect (default: 1.0)
    depth (float): The depth of the 16D effect (default: 1.0)

    Returns:
    sound_16d (numpy array): The 16D audio effect
    """
    left_channel = sound[:, 0]
    right_channel = sound[:, 1]

    channels = []
    for i in range(16):
        left_weight = (1 - i / 16) * width + (i / 16) * depth
        right_weight = (1 - i / 16) * depth + (i / 16) * width

        channel = left_channel * left_weight + right_channel * right_weight

        channel = resample(channel, int(sample_rate), axis=0)

        channels.append(channel)

    sound_16d = np.column_stack(channels)

    return sound_16d