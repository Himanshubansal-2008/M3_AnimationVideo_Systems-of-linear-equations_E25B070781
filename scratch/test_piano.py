import numpy as np
import scipy.signal as signal
import wave

sr = 44100

def note_freq(name, octave):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    semitones = notes.index(name) + (octave - 4) * 12 - 9  # A4 = 440
    return 440.0 * (2.0 ** (semitones / 12.0))

print("C4:", note_freq("C", 4))
print("E4:", note_freq("E", 4))
print("G4:", note_freq("G", 4))
