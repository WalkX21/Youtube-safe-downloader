import streamlit as st
from pytube import YouTube
import os

def download_video(video_url, download_type):
    try:
        video_object = YouTube(video_url)
        if download_type == 'MP3':
            audio_stream = video_object.streams.filter(only_audio=True).first()
            file_path = audio_stream.download()
            base, ext = os.path.splitext(file_path)
            new_file = base + '.mp3'
            os.rename(file_path, new_file)
            return new_file
        elif download_type == 'MP4':
            video_stream = video_object.streams.get_highest_resolution()
            return video_stream.download()
    except Exception as e:
        return str(e)

def main():
    st.title('YouTube Downloader')
    st.write("Minimalist app to download YouTube videos as MP3 or MP4")

    video_url = st.text_input('Enter YouTube video URL:')
    download_type = st.radio('Select format:', ('MP3', 'MP4'))

    if st.button('Download'):
        if video_url:
            with st.spinner('Downloading...'):
                file_path = download_video(video_url, download_type)
                if os.path.exists(file_path):
                    st.success('Download complete!')
                    st.write(f"File saved at: {file_path}")
                else:
                    st.error(f"Error: {file_path}")
        else:
            st.error('Please enter a valid YouTube URL.')

if __name__ == '__main__':
    main()
