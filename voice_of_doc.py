# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    return output_filepath 

input_text="Hi this is Ai with Hassan!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
"""import os
from elevenlabs.client import ElevenLabs
import uuid

def text_to_audio_elevenlabs_sdk(
    text: str,
    voice_id: str = "JBFqnCBsd6RMkjVDRZzb",
    model_id: str = "eleven_multilingual_v2",
    output_format: str = "mp3_44100_128",
    output_path: str = "elevenlabs_testing.mp3",
    api_key: str = None
) -> str:
    """  """ Converts text to speech using ElevenLabs SDK and saves it to a specified file.
    Returns:
        str: Path to the saved audio file."""    """
    try:
        api_key = api_key or os.getenv("ELEVEN_API_KEY")
        if not api_key:
            raise ValueError("ElevenLabs API key is required.")

        # Initialize client
        client = ElevenLabs(api_key=api_key)

        # Generate audio stream
        audio_stream = client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id=model_id,
            output_format=output_format
        )

        # Ensure directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        # Write audio stream to file
        with open(output_path, "wb") as f:
            for chunk in audio_stream:
                f.write(chunk)

        return output_path

    except Exception as e:
        print("Error:", e)
        raise
 

text_to_audio_elevenlabs_sdk(input_text, output_path="elevenlabs_testing.mp3") """

#model for text output to voice



import os
import platform
import subprocess
from gtts import gTTS
from pydub import AudioSegment

def text_to_speech_with_gtts_old(input_text, output_filepath="final.wav"):
    language = "en"

    # Generate speech
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    #audioobj.save(output_filepath)

    mp3_path = "temp_output.mp3"
    audioobj.save(mp3_path)
    
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(output_filepath, format="wav")

    os_name = platform.system()

    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run([
                'powershell',
                '-c',
                f'(New-Object Media.SoundPlayer "{os.path.abspath(output_filepath)}").PlaySync();'
            ])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

    return output_filepath    


input_text="Hi this is Ai with Hassan, autoplay testing!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")