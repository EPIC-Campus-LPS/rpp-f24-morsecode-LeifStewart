from pydub import AudioSegment #type: ignore

from pydub.playback import play #type: ignore

sound = AudioSegment.from_mp3("morselong.mp3")
play(sound)