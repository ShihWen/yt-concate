from pytube import YouTube

from settings import VIDEOS_DIR
from pipeline.steps.step import Step



class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        yt_set = set([found.yt for found in data])
        print(f'Videos to download:{len(yt_set)}')        

        for yt in yt_set:  
            url = yt.url
            
            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue
            print(f'downloading {url}')
            YouTube(url).streams.filter(res="720p").first().download(output_path=VIDEOS_DIR,
                                                    filename=yt.id + '.mp4'  )
        
        return data
