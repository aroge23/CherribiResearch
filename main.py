from youtubesearchpython import VideosSearch
from youtube_transcript_api import YouTubeTranscriptApi as ytapi
import json as js

query = "jahiliyyah"
videoSearch = VideosSearch(query, limit= 5)
searches = videoSearch.result()['result']

json = {}

for search in searches:

    # Time range between 2015-2019
    published = search['publishedTime']
    yearsAgo = int(published[:2])
    if (yearsAgo > 7 or yearsAgo < 3):
        print('The video {} was published {}'.format(search['title'], published))
    else:
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

# print(next(iter(json.items())))
print(js.dumps(json, indent=4))