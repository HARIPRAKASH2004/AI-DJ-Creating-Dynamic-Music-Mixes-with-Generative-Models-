from pydub import AudioSegment
import random

# Load audio tracks
track1 = AudioSegment.from_file("track1.mp3")
track2 = AudioSegment.from_file("track2.mp3")

# Define mixing function
def mix_tracks(track1, track2):
    # Get lengths of tracks
    len1 = len(track1)
    len2 = len(track2)

    # Ensure tracks have same duration
    if len1 > len2:
        track1 = track1[:len2]
    elif len2 > len1:
        track2 = track2[:len1]

    # Mix tracks
    mixed_track = track1.overlay(track2)

    return mixed_track

# Main function
def main():
    # Mix tracks
    mixed_track = mix_tracks(track1, track2)

    # Export mixed track
    mixed_track.export("mixed_track.mp3", format="mp3")

if __name__ == "__main__":
    main()
