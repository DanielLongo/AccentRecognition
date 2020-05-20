import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import flask_cors
from flask_cors import CORS, cross_origin
import logging
from score_accent import sample_recognize

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')
UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def fileUpload():
    logger.info("welcome to upload`")
    # file = request.files['file']
    file = request.files['file']
    filename = secure_filename(file.filename)
    file = file.read()
    # print("file", file)
    # filename = "testing" #
    word, confidence = sample_recognize(file)
    # print("filename", filename)
    # print("file", file)
    # destination="/".join([target, filename])
    # file.save(destination)
    # session['uploadFilePath']=destination
    # response="Whatever you wish too return"
    # print("done")
    return {"word": word, "confidence": confidence}


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)

flask_cors.CORS(app, expose_headers='Authorization')

# from flask import Flask
# from flask import request
# from test import send_audio
# import json
# from google.cloud import speech_v1p1beta1
# import os
#
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/DanielLongo/keys/lang-d5630e9c6c37.json"
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
#
# @app.route('/score_audio', methods=['POST'])
# def get_score():
#     print("received score audio request")
#     # print("data", request.files['correct_word'])
#     # data = json.loads(request.form.get('data'))
#     # print("data", data)
#     if request.method == 'POST':
#         print(request.files['messageFile'])
#         sample_recognize(request.files['messageFile'])
#
#
#     return "score audio"
#
#
# def sample_recognize(audio_blob):
#     """
#     Print confidence level for individual words in a transcription of a short audio
#     file.
#
#     Args:
#       local_file_path Path to local audio file, e.g. /path/audio.wav
#     """
#
#     client = speech_v1p1beta1.SpeechClient()
#
#     # local_file_path = 'resources/brooklyn_bridge.flac'
#
#     # When enabled, the first result returned by the API will include a list
#     # of words and the confidence level for each of those words.
#     enable_word_confidence = True
#
#     # The language of the supplied audio
#     language_code = "es-ES"
#     config = {
#         "enable_word_confidence": enable_word_confidence,
#         "language_code": language_code,
#         "audio_channel_count": 2
#
#     }
#     # with io.open(local_file_path, "rb") as f:
#     #     content = f.read()
#     #
#     audio = {"content": audio_blob}
#
#     response = client.recognize(config, audio, )
#     # The first result includes confidence levels per word
#     result = response.results[0]
#     # First alternative is the most probable result
#     alternative = result.alternatives[0]
#     print(u"Transcript: {}".format(alternative.transcript))
#     # Print the confidence level of each word
#     for word in alternative.words:
#         print(u"Word: {}".format(word.word))
#         print(u"Confidence: {}".format(word.confidence))
#
#
# if __name__ == "__main__":
#     app.run()
#     send_audio()
#
