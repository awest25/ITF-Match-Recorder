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
        '-t', '00:10:00',        # Duration to record (e.g., 10 minutes in this example)
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
    stream_url = "https://lc-live-http-ipv4.akamaized.net/14879/5014139/mobile-ireland/master_delayed.m3u8?cid=14879&mid=52018503&ecid=5014139&pid=6&dtid=1&sid=787372327810&gc=rbg&gsd=u6o&grm=1&hdnts=ip=108.228.238.242~exp=1722640242~acl=%2F14879%2F5014139%2Fmobile-ireland%2F%2A~hmac=49e5df6a7016f8cf47fe7689c13c15ead582892283774fb115624b6a38abd937"
    output_file = "livestream_recording.mp4"
    
    record_livestream(stream_url, output_file)
