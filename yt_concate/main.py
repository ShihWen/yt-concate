import ssl

from pipeline.steps.preflight import Preflight
from pipeline.steps.postflight import Postflight
from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.download_captions import DownloadCaptions
from pipeline.steps.read_captions import ReadCaptions
from pipeline.steps.step import StepException
from pipeline.pipeline import Pipeline
from utils import Utils


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
ssl._create_default_https_context = ssl._create_unverified_context

# Hello from Testrite 3 !

def main():
    input = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
    }

    steps = [ 
        Preflight(),
        GetVideoList(), 
        DownloadCaptions(),
        ReadCaptions(),
        Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(input, utils)


if __name__ == "__main__":  
    main()
