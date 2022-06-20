import ssl
from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.download_captions import DownloadCaptions
from pipeline.steps.step import StepException
from pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
ssl._create_default_https_context = ssl._create_unverified_context


def main():
    input = {
        'channel_id': CHANNEL_ID
    }

    steps = [ 
        GetVideoList(), 
        DownloadCaptions()
    ]

    p = Pipeline(steps)
    p.run(input)


if __name__ == "__main__":  
    main()
