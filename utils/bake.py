import numpy as np
from scipy.signal import resample

def effectBakeAudio(sound, sample_rate=44100, distortion_amount=20.0, noise_amount=1):
    """
    ruins the music

    Parameters:
    sound (AudioSegment): The input audio
    sample_rate (int): The sample rate of the input audio (default: 44100)
    distortion_amount (float): The amount of distortion to apply (default: 5.0)
    noise_amount (float): The amount of noise to add (default: 0.2)

    Returns:
    sound_horrible (numpy array): The horrible quality audio effect
    """
    sound_clipped = np.clip(sound, -distortion_amount, distortion_amount)

    noise = np.random.uniform(-noise_amount, noise_amount, size=sound.shape)
    sound_noisy = sound_clipped + noise

    sound_downsampled = resample(sound_noisy, int(sample_rate / 4), axis=0)

    return sound_downsampled