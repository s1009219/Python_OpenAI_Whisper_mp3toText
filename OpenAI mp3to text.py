Authorization: Bearer OPENAI_API_KEY
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Organization: org-Tkfa5laSdjnO0efhHw2Drnv1"
import openai
openai.organization = "org-Tkfa5laSdjnO0efhHw2Drnv1"
openai.api_key = <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>


curl https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@/path/to/file/audio.mp3" \
  -F model="whisper-1"

openai.Model.list()
import openai
audio_file= open(r"C:\Users\Daniel\Downloads\0912recording.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

