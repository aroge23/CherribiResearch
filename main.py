from youtubesearchpython import *
from youtube_transcript_api import YouTubeTranscriptApi as ytapi
import json as js
import csv

query = "jihad"
print('Pulling up YouTube results for the search term "{}"'.format(query))
videoSearch = VideosSearch(query, language='ur', limit=40) #try language='ur, ar, hi, pa'
searches = videoSearch.result()['result']
json = {}
searchList = []


for search in searches:
    # ==============================================================
    # Time range between 2015-2019
    # ==============================================================
    published = search['publishedTime']
    try:
        # yearsAgo = int(published[:2])
        # if (yearsAgo > 7 or yearsAgo < 3):
        #     print('The video {} was published {}'.format(search['title'], published))
        # else:

        searchjson = {}

        title = search['title']
        searchjson['title'] = title

        channel_id = search['channel']['id']
        searchjson['channel_id'] = channel_id

        channel_url = search['channel']['link']
        searchjson['channel_url'] = channel_url

        id = search['id']
        searchjson['id'] = id

        url = search['link']
        searchjson['url'] = url

        # ==============================================================
        # GET THE TRANSCRIPTS OF EACH VID
        # ==============================================================
        # try:
        #     texts = ytapi.get_transcript(id, languages=['en'])
        #     transcript = []
        #     for text in texts:
        #         transcript.append(text['text'])
        #     searchjson['text'] = transcript
        # except Exception as e:
        #     searchjson['text'] = transcript
        #     print('Error for title "{}": '.format(title), e)
        # json[title] = searchjson
        searchList.append(searchjson)
    except Exception as e:
        print('Error on search {}: {}'.format(search, e))

# ==============================================================
# PRINT ENTIRE SEARCH JSON: VID TITLE, CHANNEL ID, CHANNEL URL
# VID ID, AND VID URL
# ==============================================================
# print(js.dumps(searchList, indent=4))

# ==============================================================
# CONSOLIDATE CHANNEL URLS TO CHANNEL IDS IN A DICT
# ==============================================================
id_url = {}
for val in searchList:
    id_url[val['channel_id']] = val['channel_url']

for id, url in id_url.items():
    print('The channel id {} has a url of: {}'.format(id, url))

# ==============================================================
# WRITE TRANSCRIPTS TO A CSV FILE
# ==============================================================
# transcripts = open('transcripts.csv', 'w')
# csv_writer = csv.writer(transcripts)

# count = 0
# for key in searchList:
#     if count == 0:
#         header = key.keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(key.values())
