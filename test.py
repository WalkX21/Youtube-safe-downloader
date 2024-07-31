import streamlit as st
from pytubefix import YouTube
from pytubefix.cli import on_progress
import base64
import os
from io import BytesIO
def main():
    path = st.text_input("Enter url of your video")
    if st.button("download"):
        yt = YouTube(path, on_progress_callback = on_progress)
        st.write("Video Title:" +  str(yt.title))
        #st.write(str(yt.vid_info))
        st.write(str(yt.author))
        ys = yt.streams.get_audio_only()
        ys.download(output_path='output')
        #file_var = AudioSegment.from_ogg(uploaded_file) 
        #file_var.export('filename.wav', format='wav')
        for filename in os.listdir('output'):
            st.write(filename)
            st.download_button(
                label=f"Download {filename}",
                data=open('output'),
                file_name=filename,
                mime="video/mp4",
            )

if __name__ == '__main__':
    main()




# deposer la video dans un dossier
# lire le dossier
# telecharger la video
#supprimer la video
