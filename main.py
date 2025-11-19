from utils import read_video, save_video
from trackers import Tracker

def main ():
    # Read video
    video_frames = read_video('input_videos/real_madrid_clip.mp4')

    # Initialize tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/track_stubs.pkl')

    # Draw output
    ## Draw object Tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save video
    save_video(output_video_frames, 'output_videos/output_video2.avi')

if __name__ == "__main__":
    main()