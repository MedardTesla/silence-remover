import wave


# test1.wave

def get_16bites_sample_from_bytes(bytesLS, bytesMS):
    unsigned = bytesLS + bytesMS*256
    signed = unsigned
    if unsigned > 32767:
        signed = unsigned-65536
    return signed

def get_16bites_samples_from_bytes(bytes):
    samples = []
    for i in range(0,len(bytes)-1, 2):
        sample = get_16bites_sample_from_bytes(bytes[i], bytes[i+1])
        samples.append(sample)

    return samples


def wave_file_read_sample(filename):
    expected_n_channel = 1 # mono
    expected_sample_width = 2  # 16 bites
    expected_framerate = 44100

    wr = wave.open(filename, mode='rb')

    if wr.getnchannels() != expected_n_channel:
        print(" ERREUR: Utilisez un chiffier mono ")
        return None
    if wr.getsampwidth() != expected_sample_width:
        print(" ERREUR: Utilisez le format 16bites ")
        return None

    if wr.getframerate() != expected_framerate:
        print(" ERREUR: Utilisez la frequence 44100hz ")
        return None

    nframe = wr.getnframes()

    print(" Le nombre de frame est : ", nframe)

    frame_as_bytes = wr.readframes(nframe)

    frame_16bits = get_16bites_samples_from_bytes(frame_as_bytes)
    
    wr.close()

    return frame_16bits