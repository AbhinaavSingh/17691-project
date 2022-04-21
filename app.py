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

is_youtube_video = st.radio(
            "Is this a YouTube video?",
            ["Yes", "No"],
            help="At present, you can choose to summarize either a YouTube video or a custom video that you upload",
        )

if is_youtube_video=="Yes":
  video = st.text_input("YouTube video URL")
  video_id = video.split("=")[1]
  transcript = YouTubeTranscriptApi.get_transcript(video_id)
  submitted = st.form_submit_button(label="Summarize")
  
  text = ""
  for i in transcript:
      text += ' ' + i['text']


  summarizer = pipeline('summarization', model='facebook/bart-large-cnn', max_length=100)
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

