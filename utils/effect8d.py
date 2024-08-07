from pydub import AudioSegment
from settings import panBoundary, jumpPercentage, timeLtoR, volumeMultiplier

def panArray():
    """
    Generates an array of range -1.0 to 1.0 which control the position of the audio source (pan effect).
    -1.0 places the audio source on extreme left, 0.0 on center, and 1.0 on extreme right.
    The audio is split into multiple pieces, and each piece is played from a position decided by this array.

    Returns pan position array along with the time length of each piece to play at one position.
    """
    piecesCtoR = panBoundary / jumpPercentage
    piecesLtoR = piecesCtoR * 2
    pieceTime = int(timeLtoR / piecesLtoR)

    pan = []
    left = -panBoundary

    while left <= panBoundary:
        pan.append(left)
        left += jumpPercentage

    pan = [x / 100 for x in pan]
    return pan, pieceTime

def effect8d(sound):
    """
    Generates the 8d sound effect by splitting the audio into multiple smaller pieces,
    panning each piece to make the sound source seem like it is moving from L to R and R to L in a loop,
    and decreasing volume towards the center position to make the movement sound like it is a circle
    instead of a straight line.
    """
    pan, pieceTime = panArray()
    segments = []

    panIndex = 0
    iteratePanArrayForward = True

    for time in range(0, len(sound), pieceTime):
        piece = sound[time:time + pieceTime]

        if panIndex == 0:
            iteratePanArrayForward = True
        elif panIndex == len(pan) - 1:
            iteratePanArrayForward = False

        volAdjust = volumeMultiplier - (abs(pan[panIndex]) / (panBoundary / 100) * volumeMultiplier)
        piece = piece - volAdjust
        piece = piece.pan(pan[panIndex])

        if iteratePanArrayForward:
            panIndex += 1
        else:
            panIndex -= 1

        segments.append(piece)

    sound8d = AudioSegment.empty()
    for segment in segments:
        sound8d += segment

    return sound8d
