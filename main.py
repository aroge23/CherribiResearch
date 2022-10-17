from youtubesearchpython import *
from youtube_transcript_api import YouTubeTranscriptApi as ytapi
import json as js
import csv

query = "jihad"
videoSearch = VideosSearch(query, language='ur', limit=40) #try language='ur, ar, hi, pa'
searches = videoSearch.result()['result']
# print(js.dumps(searches[0], indent=4))
json = {}
searchList = []


for search in searches:
    # print(js.dumps(search, indent=4))
    # Time range between 2015-2019
    published = search['publishedTime']
    try:
        yearsAgo = int(published[:2])
        # if (yearsAgo > 7 or yearsAgo < 3):
        #     print('The video {} was published {}'.format(search['title'], published))
        # else:
        searchjson = {}

        title = search['title']
        searchjson['title'] = title

        channel_id = search['channel']['id']
        searchjson['channel_id'] = channel_id

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
        searchList.append(searchjson)
    except Exception as e:
        print('Error on search {}: {}'.format(search, e))

# print(next(iter(json.items())))
# print(js.dumps(json, indent=4))
print(js.dumps(searchList, indent=4))

# transcripts = open('transcripts.csv', 'w')
# csv_writer = csv.writer(transcripts)

# count = 0
# for key in searchList:
#     if count == 0:
#         header = key.keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(key.values())
