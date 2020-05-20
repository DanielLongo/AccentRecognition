from google.cloud import speech_v1p1beta1
# from pydub import AudioSegment
# import io
import os
# import sys
# sys.path.append('/path/to/ffmpeg')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
client = speech_v1p1beta1.SpeechClient()

def sample_recognize(input_audio):
    """
    Print confidence level for individual words in a transcription of a short audio
    file.

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    # local_file_path = 'resources/brooklyn_bridge.flac'

    # When enabled, the first result returned by the API will include a list
    # of words and the confidence level for each of those words.
    enable_word_confidence = True

    # The language of the supplied audio
    # language_code = "es-ES"
    language_code= "es-CO"
    config = {
        "enable_word_confidence": enable_word_confidence,
        "language_code": language_code,
        "audio_channel_count": 1,
    }
    # print(type(input_audio))
    # song = AudioSegment.from_file(io.BytesIO(input_audio), format="wav")
    # song.export("tmp.wav", format="wav")
    # with io.open("tmp.wav", "rb") as f:
    #     content = f.read()
    # # print(type(song))
    # audio = {"content": content}

    audio = {"content": input_audio}

    response = client.recognize(config, audio, )
    print("response", response)
    # print("response", response)
    # The first result includes confidence levels per word
    # print("result", response.results)

    # First alternative is the most probable result
    try:
        result = response.results[0]
    except IndexError:
        # No matches found
        return "FAILED", 0
    alternative = result.alternatives[0]
    # print(u"Transcript: {}".format(alternative.transcript))
    # # Print the confidence level of each word
    for word in alternative.words:
        return word.word, word.confidence
        # if word.confidence > .4:
        #     return word.word
    return "FAILED", 0
        # print("word", word.word)
        # print("Confidence", word.confidence)
        # print(u"Word: {}".format(word.word))
        # print(u"Confidence: {}".format(word.confidence))
