# 5-minute Mathematical Transformations video (Manim + male AI voice)

## 1. Activate your virtual environment
source venv/bin/activate

## 2. Install packages
python -m pip install manim manim-voiceover edge-tts mutagen

## 3. Generate the male AI voice clips
python generate_voice.py

The default voice is Microsoft Edge TTS `en-US-GuyNeural` (male).
Alternative: change VOICE in generate_voice.py to `en-GB-RyanNeural`.

## 4. Render the video
python -m manim -pqh main.py MathematicalTransformations

For a quicker preview, use:
python -m manim -pql main.py MathematicalTransformations

The rendered MP4 is placed in Manim's media/videos folder.

Notes:
- Edge TTS requires an internet connection.
- The video is padded to at least 300 seconds (5 minutes). If the generated narration itself takes longer than five minutes, the output will be longer.
- Seven narration clips are generated, including a separate recap. The video is padded to at least 300 seconds (5 minutes); brief scene transitions may make it a few seconds longer.
