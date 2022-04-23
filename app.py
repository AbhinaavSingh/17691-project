import streamlit as st
import numpy as np
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

st.set_page_config(
    page_title="Video Transcript Summarizer",
    page_icon="🎈",
    layout = "centered"
)

st.title("Video transcript Summarizer!")

col1, col2 = st.columns(2)

with col1:
    video_type = st.selectbox(
            "Select video type", ("YouTube", "Video Upload")
        )

with col2:
    is_research_video = st.selectbox(
            "Research Video", ("Yes", "No")
        )

if video_type=="YouTube":
video = st.text_input("YouTube video URL")
#submitted = st.form_submit_button(label="Summarize")
if submitted:
  video_id = video.split("=")[1]
  transcript = YouTubeTranscriptApi.get_transcript(video_id)
  text = ""
  for i in transcript:
      text += ' ' + i['text']

  st.write("Preparing your summary...")
  st.write("Transformer at work...")
  summarizer = pipeline('summarization')

  num_iters = int(len(text)/1000)
  summarized_text = []
  for i in range(0, num_iters + 1):
    start = 0
    start = i * 1000
    end = (i + 1) * 1000
    out = summarizer(text[start:end])[0]['summary_text']
    summarized_text.append(out)

  st.write("SUMMARY")
  st.write(str(summarized_text))

if video_type=="Video Upload":
    video = st.file_uploader(label="Upload your video")
    if video is not None:
        st.write(video)
    
