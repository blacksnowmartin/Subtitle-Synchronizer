import moviepy.editor as mp
import pysrt

def synchronize_subtitles(video_path, subtitle_path, output_subtitle_path, delay_seconds):
    # Load video
    video = mp.VideoFileClip(video_path)
    
    # Load subtitles
    subs = pysrt.open(subtitle_path)
    
    # Adjust subtitles timing
    for sub in subs:
        sub.start.shift(seconds=delay_seconds)
        sub.end.shift(seconds=delay_seconds)
    
    # Save synchronized subtitles
    subs.save(output_subtitle_path, encoding='utf-8')

if __name__ == "__main__":
    # Path to the input video file
    video_path = "input_video.mp4"
    
    # Path to the input subtitle file (SRT format)
    subtitle_path = "input_subtitles.srt"
    
    # Path to the output subtitle file (SRT format)
    output_subtitle_path = "output_subtitles.srt"
    
    # Delay in seconds (positive value delays the subtitles, negative value advances them)
    delay_seconds = 2.0  # Adjust this value as needed
    
    # Synchronize subtitles
    synchronize_subtitles(video_path, subtitle_path, output_subtitle_path, delay_seconds)
    
    print(f"Subtitles synchronized and saved to {output_subtitle_path}")
