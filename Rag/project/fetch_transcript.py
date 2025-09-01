from youtube_transcript_api import YouTubeTranscriptApi
from langchain.schema import Document

video_id = "DPmtnb8NBog"

ytt_api = YouTubeTranscriptApi()

try:
    fetched_transcript = ytt_api.fetch(video_id)
    snippets = fetched_transcript.snippets
    formatted_transcript = [
        {"text": snippet.text, "start": snippet.start, "duration": snippet.duration}
        for snippet in snippets
    ]

    # Save to a text file
    with open("transcript.txt", "w", encoding="utf-8") as f:
        for item in formatted_transcript:
            line = f"{item['text']}'"
            f.write(line)

    print("Transcript saved to transcript.txt")
except Exception as e:
    print(f"Error: {e}")

#  JSON
# from youtube_transcript_api import YouTubeTranscriptApi
# from langchain.schema import Document
# import json
# video_id = "DPmtnb8NBog"

# ytt_api = YouTubeTranscriptApi()

# try:
#     fetched_transcript = ytt_api.fetch(video_id)
#     snippets = fetched_transcript.snippets
#     formatted_transcript = [
#         {"text": snippet.text, "start": snippet.start, "duration": snippet.duration}
#         for snippet in snippets
#     ]
#     with open("transcript.json", "w", encoding="utf-8") as f:
#         json.dump(formatted_transcript, f, ensure_ascii=False, indent=4)
#     print("Transcript saved to transcript.json")
# except Exception as e:
#     print(f"Error: {e}")
