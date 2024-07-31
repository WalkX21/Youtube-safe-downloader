import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
from pydub import AudioSegment

def main():
    path = st.text_input("Enter URL of your video")
    if st.button("Download"):
        yt = YouTube(path, on_progress_callback=on_progress)
        st.write("Video Title: " + str(yt.title))
        st.write("Author: " + str(yt.author))
        
        # Get audio stream
        ys = yt.streams.get_audio_only()
        
        # Define output path and file name
        output_path = '/workspaces/Youtube-safe-downloader/output'
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        file_path = ys.download(output_path=output_path)
        
        # Display the file name
        filename = os.path.basename(file_path)
        st.write("Downloaded:", filename)

        mp3_file_path = os.path.join(output_path, os.path.splitext(os.path.basename(file_path))[0] + '.mp3')
        audio = AudioSegment.from_file(file_path)
        audio.export(mp3_file_path, format='mp3')
        
        # Provide download button
        with open(mp3_file_path, 'rb') as f:
            st.download_button(
                label=f"Download {mp3_file_path}",
                data=f,
                file_name=mp3_file_path,
                mime="audio/mp4"
            )
        
        # Optional: Clean up downloaded files
        # print(output_path)
        # print(mp3_file_path)
        os.remove(mp3_file_path)
        os.remove(file_path)

if __name__ == '__main__':
    main()
