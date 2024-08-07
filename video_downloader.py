import subprocess
import sys

def record_livestream(stream_url, output_file):
    """
    Records a livestream from the given URL and saves it to the specified output file.

    Parameters:
    - stream_url (str): The URL of the livestream.
    - output_file (str): The path to the output file where the recording will be saved.
    """
    # Command to record the livestream using ffmpeg
    command = [
        'ffmpeg',
        '-i', stream_url,        # Input URL
        '-c', 'copy',            # Copy the codec (do not re-encode)
        '-t', '03:00:00',        # Duration to record (e.g., 3 hours in this example)
        output_file
    ]
    
    try:
        # Execute the ffmpeg command
        subprocess.run(command, check=True)
        print(f"Recording saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error recording livestream: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Example usage
    stream_url = "https://lc-live-http-euw1-ipv4-p.hs.llnwd.net/e1/lt/limelight/5042293/mobile-ireland/token=p=85~e=1723158096~ip=104.2.24.180~cid=14879~mid=52285499~ecid=5042293~pid=6~dtid=1~sid=917500152047~gc=TTY~gsd=WyQ~grm=1~h=958618086d3b435f86b714385ebb5420/master_delayed.m3u8"
    output_file = "out/livestream_recording.mp4"
    
    record_livestream(stream_url, output_file)
