from youtubesearchpython import VideosSearch
from youtube_transcript_api import YouTubeTranscriptApi as ytapi

videoSearch = VideosSearch("jahiliyyah", limit= 5)
searches = videoSearch.result()['result']

json = {}

for search in searches:
    title = search['title']

    searchjson = {}

    id = search['id']
    searchjson['id'] = id

    url = search['link']
    searchjson['url'] = url

    try:
        texts = ytapi.get_transcript(id, languages=['en'])
        transcript = []
        for text in texts:
            transcript.append(text['text'])
        searchjson['text'] = transcript
    except Exception as e:
        searchjson['text'] = transcript
        print('Error for title "{}": '.format(title), e)
    json[title] = searchjson

print(json)