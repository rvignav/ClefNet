import math
import os
import sys
import traceback

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from scipy.fftpack import rfft, irfft
from glob import iglob
from pydub import AudioSegment

DATA_FILES_MP3 = 'audio'
DATA_FILES_WAV = 'audio_wav'
file_arr = []
curr_batch = 0


def convert_mp3_to_wav():
    index = 0
    for file in iglob(DATA_FILES_MP3 + '/*.mp3'):
        print("begin convert " + file)
        mp3_to_wav = AudioSegment.from_mp3(file)
        print("finished convert " + file + ". Now exporting file to audio_wav")
        mp3_to_wav.export(DATA_FILES_WAV + '/' + str(index) + '.wav', format='wav')
        print("export to audio_wav for " + file + " success")
        index += 1


def process_wav():
    if os.path.isfile(DATA_FILES_WAV):
        convert_mp3_to_wav()
    for file in iglob(DATA_FILES_WAV + '/*.wav'):
        file_arr.append(file)


def get_next_batch(curr_batch, songs_per_batch, sess):
    wav_arr_ch1 = []
    wav_arr_ch2 = []
    if curr_batch >= (len(file_arr)):
        curr_batch = 0

    start_position = curr_batch * songs_per_batch
    end_position = start_position + songs_per_batch
    for idx in range(start_position, end_position):
        try:
            audio_binary = tf.io.read_file(file_arr[idx])
        except:
            print(file_arr)
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)
            exit(0)
        wav_decoder = tf.audio.decode_wav(
            audio_binary,
            desired_channels=2)
        sample_rate, audio = sess.run([wav_decoder.sample_rate, wav_decoder.audio])
        audio = np.array(audio)

        if len(audio[:, 0]) != 5292000:
            continue

        wav_arr_ch1.append(rfft(audio[:, 0]))
        wav_arr_ch2.append(rfft(audio[:, 1]))
        print("Returning File: " + file_arr[idx])

    return wav_arr_ch1, wav_arr_ch2, sample_rate


def save_to_wav(audio_arr_ch1, audio_arr_ch2, sample_rate, original_song_ch1, original_song_ch2, idty, folder, sess):
    audio_arr_ch1 = irfft(np.hstack(np.hstack(audio_arr_ch1)))
    audio_arr_ch2 = irfft(np.hstack(np.hstack(audio_arr_ch2)))

    original_song_ch1 = irfft(np.hstack(np.hstack(original_song_ch1)))
    original_song_ch2 = irfft(np.hstack(np.hstack(original_song_ch2)))

    original_song = np.hstack(np.array((original_song_ch1, original_song_ch2)).T)
    audio_arr = np.hstack(np.array((audio_arr_ch1, audio_arr_ch2)).T)

    print(original_song)
    w = np.linspace(0, sample_rate, len(audio_arr))
    w = w[0:len(audio_arr)]
    plt.figure(1)

    plt.plot(w, original_song)
    plt.savefig(str(folder) + '/original.png')
    plt.plot(w, audio_arr)
    plt.xlabel('sample')
    plt.ylabel('amplitude')
    plt.savefig(str(folder) + '/compressed' + str(idty) + '.png')
    plt.clf()

    cols = 2
    rows = math.floor(len(audio_arr) / 2)
    audio_arr = audio_arr.reshape(rows, cols)
    original_song = original_song.reshape(rows, cols)

    wav_encoder = tf.audio.encode_wav(audio_arr, sample_rate=sample_rate)
    wav_encoder_orig = tf.audio.encode_wav(original_song, sample_rate=sample_rate)

    wav_file = sess.run(wav_encoder)
    wav_orig = sess.run(wav_encoder_orig)
    open(str(folder) + '/out.wav', 'wb').write(wav_file)
    open(str(folder) + '/wav_orig.wav', 'wb').write(wav_orig)
