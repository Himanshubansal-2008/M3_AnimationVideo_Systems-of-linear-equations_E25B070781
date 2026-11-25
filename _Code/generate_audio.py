"""
_Code/generate_audio.py
Synthesizes a high-quality 300-second (exact 5:00) neo-classical acoustic piano
and warm ambient strings soundtrack engineered specifically for educational voiceover.

Key Acoustic Engineering Features:
1. Physical Modeling Additive Synthesis:
   - Piano string inharmonicity (B = 0.00014)
   - Partial-dependent exponential decay (higher harmonics decay faster)
   - Dual-string chorus detuning (warm acoustic singing tone)
   - Soft hammer felt attack transient
2. Warm Ambient Bowed String Foundation:
   - Detuned multi-voice cello & violin string pads with gentle swell envelopes
3. Vocal Pocket Engineering:
   - Wide parametric attenuation across 1.0 kHz - 2.8 kHz (the human speech presence zone)
   - Stereo width leaving dead-center open for speech
   - Low-cut at 60 Hz to remove sub-bass rumble
   - Mastered to gentle -23.5 dB RMS background level
"""

import numpy as np
import scipy.signal as signal
import wave
import os

def note_freq(name, octave):
    """Calculates equal temperament frequency for note name and octave."""
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    semitones = notes.index(name) + (octave - 4) * 12 - 9  # A4 = 440 Hz
    return 440.0 * (2.0 ** (semitones / 12.0))

def synthesize_piano_note(freq, duration, velocity=0.7, sr=44100):
    """
    Synthesizes a realistic acoustic piano note using physical modeling principles.
    Inharmonic partials, partial-dependent decay, and dual-string beating.
    """
    n_samples = int(duration * sr)
    if n_samples <= 0:
        return np.zeros(0, dtype=np.float32)
        
    t = np.linspace(0, duration, n_samples, endpoint=False)
    
    # Inharmonicity parameter for piano strings
    B = 0.00014
    
    # 2 slightly detuned strings struck by the hammer (creates natural acoustic chorus)
    detunes = [-0.15, 0.15]
    note = np.zeros(n_samples, dtype=np.float32)
    
    # Number of harmonics based on frequency
    max_harmonics = min(15, int(sr / (2.5 * freq)))
    
    for detune in detunes:
        for h in range(1, max_harmonics + 1):
            # Inharmonic frequency formula: f_n = n * f0 * sqrt(1 + B * n^2)
            f_h = h * freq * np.sqrt(1.0 + B * (h ** 2)) + detune
            if f_h >= sr / 2.1:
                break
                
            # Decay rate increases with harmonic order
            decay = (0.75 + 0.38 * h + 0.0012 * freq) * (1.15 - 0.25 * velocity)
            amp = (1.0 / (h ** 1.3)) * np.exp(-decay * t)
            
            # Subtle initial phase dispersion
            phase = (h * 0.73) % (2 * np.pi)
            note += amp * np.sin(2.0 * np.pi * f_h * t + phase)
            
    # Soft felt hammer transient
    hammer_samples = int(0.012 * sr)
    if hammer_samples < n_samples:
        np.random.seed(int(freq * 100) % 10000)
        hammer = np.random.normal(0, 0.04, hammer_samples)
        hammer *= np.hanning(hammer_samples * 2)[hammer_samples:]
        note[:hammer_samples] += hammer * velocity
        
    # Attack envelope (smooth 3.5ms ramp to prevent clicks)
    attack_samples = int(0.0035 * sr)
    if attack_samples < n_samples:
        note[:attack_samples] *= np.linspace(0, 1, attack_samples)
        
    # Scaling
    note *= (velocity * 0.08)
    return note

def synthesize_warm_strings_chord(freqs, duration, velocity=0.45, sr=44100):
    """
    Synthesizes a soft, warm ambient string pad chord.
    Rich detuned oscillators with gentle low-pass filtering.
    """
    n_samples = int(duration * sr)
    if n_samples <= 0:
        return np.zeros(0, dtype=np.float32)
        
    t = np.linspace(0, duration, n_samples, endpoint=False)
    chord = np.zeros(n_samples, dtype=np.float32)
    
    for freq in freqs:
        # Multiple detuned voices for string ensemble thickness
        voices = [-0.4, 0.0, 0.4]
        for v_detune in voices:
            f = freq + v_detune
            # Fundamental + soft harmonics
            w1 = np.sin(2.0 * np.pi * f * t)
            w2 = 0.35 * np.sin(4.0 * np.pi * f * t)
            w3 = 0.15 * np.sin(6.0 * np.pi * f * t)
            w4 = 0.08 * np.sin(8.0 * np.pi * f * t)
            chord += (w1 + w2 + w3 + w4)
            
    # Gentle swell attack and release envelope (1.8s attack, 2.0s release)
    env = np.ones(n_samples, dtype=np.float32)
    att_len = min(int(1.8 * sr), n_samples // 3)
    rel_len = min(int(2.0 * sr), n_samples // 3)
    
    if att_len > 0:
        env[:att_len] = 0.5 * (1.0 - np.cos(np.pi * np.linspace(0, 1, att_len)))
    if rel_len > 0:
        env[-rel_len:] = 0.5 * (1.0 + np.cos(np.pi * np.linspace(0, 1, rel_len)))
        
    chord *= (env * velocity * 0.035 / max(len(freqs), 1))
    
    # Warm acoustic lowpass filter (Butterworth 2nd order at 850 Hz)
    sos = signal.butter(2, 850, 'lowpass', fs=sr, output='sos')
    filtered_chord = signal.sosfilt(sos, chord)
    return filtered_chord

def generate_educational_soundtrack(filename="_Code/ambient_mild_track.wav", duration=300.0, sr=44100):
    """
    Arranges and mixes a 300-second neo-classical soundtrack:
    - Flowing piano arpeggios
    - Warm ambient string pads
    - Vocal pocket EQ notch
    - Mastered to gentle -23.5 dB RMS for speech clarity
    """
    print(f"[AUDIO] Generating neo-classical voiceover soundtrack ({duration}s)...")
    num_samples = int(duration * sr)
    
    # Left and Right stereo channels
    left_channel = np.zeros(num_samples, dtype=np.float32)
    right_channel = np.zeros(num_samples, dtype=np.float32)
    
    # Tempo: 72 BPM -> 1 beat = 60/72 = 0.8333s; 1 bar of 4/4 = 3.3333s
    beat_sec = 60.0 / 72.0
    bar_sec = 4.0 * beat_sec  # ~3.333s
    
    # Chord progressions structured into 8-bar musical phrases (26.67 seconds per phrase):
    # Phrase A: C major add9 -> Am9 -> Fmaj7 -> Gsus4 -> C/E -> Dm9 -> G7 -> C
    # Phrase B: Em7 -> Fmaj9 -> Am7 -> Gsus4 -> C -> Dm7 -> G7 -> C
    
    phrase_definitions = [
        # Phrase A (Contemplative & Curious)
        [
            {"bass": ("C", 2), "pad": [("C", 3), ("G", 3), ("E", 4)], "arp": [("C", 3), ("G", 3), ("D", 4), ("E", 4), ("G", 4), ("E", 4), ("D", 4), ("G", 3)]},
            {"bass": ("A", 1), "pad": [("A", 2), ("E", 3), ("C", 4)], "arp": [("A", 2), ("E", 3), ("B", 3), ("C", 4), ("E", 4), ("C", 4), ("B", 3), ("E", 3)]},
            {"bass": ("F", 1), "pad": [("F", 2), ("C", 3), ("A", 3)], "arp": [("F", 2), ("C", 3), ("G", 3), ("A", 3), ("C", 4), ("A", 3), ("G", 3), ("C", 3)]},
            {"bass": ("G", 1), "pad": [("G", 2), ("D", 3), ("B", 3)], "arp": [("G", 2), ("D", 3), ("G", 3), ("C", 4), ("B", 3), ("G", 3), ("D", 3), ("B", 2)]},
            {"bass": ("E", 1), "pad": [("E", 2), ("B", 2), ("G", 3)], "arp": [("E", 2), ("B", 2), ("G", 3), ("B", 3), ("D", 4), ("B", 3), ("G", 3), ("B", 2)]},
            {"bass": ("D", 2), "pad": [("D", 3), ("A", 3), ("F", 4)], "arp": [("D", 2), ("A", 2), ("E", 3), ("F", 3), ("A", 3), ("C", 4), ("A", 3), ("F", 3)]},
            {"bass": ("G", 1), "pad": [("G", 2), ("D", 3), ("F", 3)], "arp": [("G", 2), ("D", 3), ("F", 3), ("A", 3), ("B", 3), ("D", 4), ("B", 3), ("G", 3)]},
            {"bass": ("C", 2), "pad": [("C", 3), ("G", 3), ("E", 4)], "arp": [("C", 2), ("G", 2), ("E", 3), ("G", 3), ("C", 4), ("E", 4), ("C", 4), ("G", 3)]},
        ],
        # Phrase B (Inspirational & Deep Insight)
        [
            {"bass": ("A", 1), "pad": [("A", 2), ("E", 3), ("C", 4)], "arp": [("A", 2), ("E", 3), ("C", 4), ("E", 4), ("G", 4), ("E", 4), ("C", 4), ("E", 3)]},
            {"bass": ("F", 1), "pad": [("F", 2), ("C", 3), ("A", 3)], "arp": [("F", 2), ("C", 3), ("A", 3), ("E", 4), ("F", 4), ("C", 4), ("A", 3), ("C", 3)]},
            {"bass": ("C", 2), "pad": [("C", 3), ("G", 3), ("E", 4)], "arp": [("C", 2), ("G", 2), ("E", 3), ("G", 3), ("D", 4), ("E", 4), ("C", 4), ("G", 3)]},
            {"bass": ("G", 1), "pad": [("G", 2), ("D", 3), ("B", 3)], "arp": [("G", 2), ("D", 3), ("B", 3), ("D", 4), ("G", 4), ("D", 4), ("B", 3), ("D", 3)]},
            {"bass": ("D", 2), "pad": [("D", 3), ("A", 3), ("F", 4)], "arp": [("D", 2), ("A", 2), ("F", 3), ("A", 3), ("C", 4), ("E", 4), ("C", 4), ("A", 3)]},
            {"bass": ("E", 1), "pad": [("E", 2), ("B", 2), ("G", 3)], "arp": [("E", 2), ("B", 2), ("G", 3), ("D", 4), ("E", 4), ("B", 3), ("G", 3), ("B", 2)]},
            {"bass": ("F", 1), "pad": [("F", 2), ("C", 3), ("A", 3)], "arp": [("F", 2), ("C", 3), ("G", 3), ("A", 3), ("C", 4), ("E", 4), ("D", 4), ("C", 4)]},
            {"bass": ("G", 1), "pad": [("G", 2), ("D", 3), ("B", 3)], "arp": [("G", 2), ("D", 3), ("G", 3), ("B", 3), ("D", 4), ("B", 3), ("A", 3), ("G", 3)]},
        ]
    ]
    
    # Total bars needed for 300 seconds: 300 / 3.3333 = 90 bars
    # We cycle between Phrase A and Phrase B with dynamic density
    num_phrases = int(np.ceil(duration / (8 * bar_sec)))
    
    current_time = 0.0
    bar_index = 0
    
    while current_time < duration:
        phrase_type = (bar_index // 8) % 2
        phrase = phrase_definitions[phrase_type]
        bar_in_phrase = bar_index % 8
        bar_data = phrase[bar_in_phrase]
        
        # 1. Synthesize Bass Note (warm piano low end, slightly left-centered)
        b_name, b_oct = bar_data["bass"]
        b_freq = note_freq(b_name, b_oct)
        bass_sound = synthesize_piano_note(b_freq, duration=bar_sec * 1.2, velocity=0.65, sr=sr)
        
        start_idx = int(current_time * sr)
        end_idx = min(start_idx + len(bass_sound), num_samples)
        chunk_len = end_idx - start_idx
        
        if chunk_len > 0:
            left_channel[start_idx:end_idx] += bass_sound[:chunk_len] * 0.6
            right_channel[start_idx:end_idx] += bass_sound[:chunk_len] * 0.4
            
        # 2. Synthesize Strings Pad (gentle swell across the entire bar, wide stereo)
        pad_freqs = [note_freq(n, o) for n, o in bar_data["pad"]]
        strings_sound = synthesize_warm_strings_chord(pad_freqs, duration=bar_sec * 1.15, velocity=0.45, sr=sr)
        
        s_end_idx = min(start_idx + len(strings_sound), num_samples)
        s_chunk = s_end_idx - start_idx
        if s_chunk > 0:
            left_channel[start_idx:s_end_idx] += strings_sound[:s_chunk] * 0.7
            right_channel[start_idx:s_end_idx] += strings_sound[:s_chunk] * 0.7
            
        # 3. Synthesize Arpeggio Notes (8 eighth notes per bar)
        arp_notes = bar_data["arp"]
        step_sec = bar_sec / len(arp_notes)
        
        for step_i, (n_name, n_oct) in enumerate(arp_notes):
            n_time = current_time + step_i * step_sec
            if n_time >= duration:
                break
                
            n_freq = note_freq(n_name, n_oct)
            # Subtle humanization in velocity
            vel = 0.52 + 0.12 * np.sin(step_i * 1.2)
            n_sound = synthesize_piano_note(n_freq, duration=2.2, velocity=vel, sr=sr)
            
            n_start = int(n_time * sr)
            n_end = min(n_start + len(n_sound), num_samples)
            n_chunk = n_end - n_start
            
            if n_chunk > 0:
                # Gentle alternating stereo pan (-0.25 to +0.25)
                pan = 0.5 + 0.22 * np.sin(step_i * 0.8)
                left_channel[n_start:n_end] += n_sound[:n_chunk] * (1.0 - pan)
                right_channel[n_start:n_end] += n_sound[:n_chunk] * pan
                
        current_time += bar_sec
        bar_index += 1

    print("[AUDIO] Applying acoustic mastering and Vocal Pocket EQ...")
    
    # ----------------------------------------------------
    # Acoustic Post-Processing & Vocal Pocket EQ
    # ----------------------------------------------------
    # 1. High-Pass Filter (Butterworth 2nd order at 55 Hz to eliminate sub-bass mud)
    sos_hp = signal.butter(2, 55, 'highpass', fs=sr, output='sos')
    left_channel = signal.sosfilt(sos_hp, left_channel)
    right_channel = signal.sosfilt(sos_hp, right_channel)
    
    # 2. Vocal Pocket EQ Notch: Attenuate 1.2 kHz - 2.8 kHz by ~4 dB
    # Human voice clarity and presence thrives here; carving this out prevents any vocal masking!
    f_center = 1800.0
    q_val = 1.2
    b_notch, a_notch = signal.iirpeak(f_center, q_val, fs=sr)
    # Dip by subtracting a fraction of the bandpass energy
    left_band = signal.lfilter(b_notch, a_notch, left_channel)
    right_band = signal.lfilter(b_notch, a_notch, right_channel)
    left_channel -= (left_band * 0.40)
    right_channel -= (right_band * 0.40)
    
    # 3. Master Smooth Fades: 3.5s Fade-In, 4.5s Fade-Out
    fade_in_samples = int(3.5 * sr)
    fade_out_samples = int(4.5 * sr)
    fade_in_curve = 0.5 * (1.0 - np.cos(np.pi * np.linspace(0, 1, fade_in_samples)))
    fade_out_curve = 0.5 * (1.0 + np.cos(np.pi * np.linspace(0, 1, fade_out_samples)))
    
    left_channel[:fade_in_samples] *= fade_in_curve
    right_channel[:fade_in_samples] *= fade_in_curve
    left_channel[-fade_out_samples:] *= fade_out_curve
    right_channel[-fade_out_samples:] *= fade_out_curve
    
    # 4. Master Volume Normalization for Voiceover
    # Target: RMS at -23.5 dBFS (standard background music level beneath speech)
    # Peak limited safely below -3 dBFS (0.7) to guarantee zero distortion.
    cur_rms = np.sqrt(np.mean((left_channel**2 + right_channel**2) / 2.0))
    target_rms = 10.0 ** (-23.5 / 20.0)
    gain = target_rms / max(cur_rms, 1e-6)
    left_channel *= gain
    right_channel *= gain

    # Soft clip limiter if any peak exceeds 0.70
    peak = max(np.max(np.abs(left_channel)), np.max(np.abs(right_channel)))
    if peak > 0.70:
        limiter = 0.70 / peak
        left_channel *= limiter
        right_channel *= limiter
        
    final_rms = 20.0 * np.log10(np.sqrt(np.mean((left_channel**2 + right_channel**2) / 2.0)))
    final_peak = max(np.max(np.abs(left_channel)), np.max(np.abs(right_channel)))
    print(f"[AUDIO] Mastered track RMS: {final_rms:.2f} dBFS, Peak: {final_peak:.2f} (Ideal vocal headroom).")
    
    # Convert to 16-bit PCM Stereo WAV
    int_left = np.int16(np.clip(left_channel, -1.0, 1.0) * 32767)
    int_right = np.int16(np.clip(right_channel, -1.0, 1.0) * 32767)
    
    stereo_data = np.empty((num_samples * 2,), dtype=np.int16)
    stereo_data[0::2] = int_left
    stereo_data[1::2] = int_right
    
    os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)
    with wave.open(filename, "wb") as wav_out:
        wav_out.setnchannels(2)
        wav_out.setsampwidth(2)
        wav_out.setframerate(sr)
        wav_out.writeframes(stereo_data.tobytes())
        
    print(f"[OK] Saved voiceover-optimized soundtrack: {filename} (Duration: {duration:.2f}s).")

if __name__ == "__main__":
    generate_educational_soundtrack("_Code/ambient_mild_track.wav", 300.0)
