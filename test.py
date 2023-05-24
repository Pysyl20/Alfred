import os


os.system('youtube-dl --output "mp3/%(title)s.%(ext)s" --extract-audio --audio-format mp3 https://www.youtube.com/watch?v=ByFLkUQZaNc')