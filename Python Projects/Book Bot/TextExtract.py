import subprocess
import os

def extract_transcript_and_process():
    """
    Prompts the user for a YouTube video link, extracts its transcript,
    and pipes it to `fabric` for further processing.
    """
    try:
        # Prompt user for the YouTube video link
        video_link = input("Enter the YouTube video link: ").strip()

        if not video_link.startswith("https://www.youtube.com/watch?v="):
            print("Invalid YouTube link. Please provide a valid link.")
            return

        # Extract the video ID
        video_id = video_link.split("v=")[-1]

        # Define the command to fetch the transcript using yt-dlp
        yt_dlp_command = [
            "yt-dlp",
            "--write-auto-sub",
            "--sub-lang", "en",
            "--skip-download",
            video_link
        ]

        # Run yt-dlp to get the transcript
        print("Fetching transcript using yt-dlp...")
        subprocess.run(yt_dlp_command, check=True)

        # Look for the generated .vtt file
        vtt_filename = f"{video_id}.en.vtt"
        if not os.path.exists(vtt_filename):
            print("Transcript file not found. Something went wrong.")
            return

        # Convert .vtt to plain text
        print("Converting .vtt file to plain text...")
        with open(vtt_filename, "r", encoding="utf-8") as vtt_file:
            lines = vtt_file.readlines()

        # Extract the meaningful lines (skip metadata)
        transcript_text = "".join(line for line in lines if not line.strip().isdigit() and "-->" not in line)

        # Pipe the transcript to fabric for further processing
        print("Piping transcript to fabric...")
        fabric_command = ["fabric", "-sp", "extract_wisdom"]
        subprocess.run(fabric_command, input=transcript_text, text=True, check=True)

        # Cleanup the .vtt file
        os.remove(vtt_filename)
        print("Process completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running a subprocess: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    extract_transcript_and_process()
