import ssl

from pipeline.steps.preflight import Preflight
from pipeline.steps.postflight import Postflight
from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.initialize_yt import InitializeYT
from pipeline.steps.download_captions import DownloadCaptions
from pipeline.steps.read_captions import ReadCaptions
from pipeline.steps.search import Search
from pipeline.steps.download_video import DownloadVideos
from pipeline.steps.edit_video import EditVideos
from pipeline.steps.step import StepException
from pipeline.pipeline import Pipeline
from utils import Utils


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
ssl._create_default_https_context = ssl._create_unverified_context

# This is multi-threads branch 

def main():
    input = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
    }

    steps = [
        Preflight(),
        GetVideoList(), 
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        EditVideos(),
        #Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(input, utils)


if __name__ == "__main__":  
    main()
