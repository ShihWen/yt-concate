from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor

from settings import VIDEOS_DIR
from pipeline.steps.step import Step




class DownloadVideos(Step):
    def download_video(self, yt, utils):
        url = yt.url
        
        if utils.video_file_exists(yt):
            print(f'found existing video file for {url}, skipping')
            return False
            
        print(f'downloading {url}')
        YouTube(url).streams.filter(res="360p").first().download(output_path=VIDEOS_DIR,
                                                filename=yt.id + '.mp4'  )

    def process(self, data, inputs, utils):

        yt_set = set([found.yt for found in data])
        print(f'Videos to download:{len(yt_set)}')        

        processes = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            for yt in yt_set:  
                processes.append(executor.submit(self.download_video, yt, utils))       
   
        
        return data
