# shazam-python
an implementation of shazam's audio-recognition algorithm


## Setup
- Install requirements with Poetry: `poetry install`
- Collect all .wav files of audio snippets into `data/samples/` folder.
- Copy all audio samples to the database: `python copy_to_db.py`
- Copy the audo recording to be matched to the `data/recordings/` folder.
- Find a match for the recording in the database: `python main.py`