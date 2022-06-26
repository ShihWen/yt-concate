from pytube import YouTube
import os
import time
from concurrent.futures import ThreadPoolExecutor

from pipeline.steps.step import Step
from pipeline.steps.step import StepException



class DownloadCaptions(Step):
    def __init__(self):
        pass


    def download_captions(self, yt, utils):
        #print(f'downloading captions for {yt.id}')
        if utils.caption_file_exists(yt):
            print(f'file exists: {yt.url}')
            return False
        
        try:
            source = YouTube(yt.url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt =(en_caption.generate_srt_captions())

        except (KeyError, AttributeError) as e:
            print(f'Error when downloading caption for {yt.url}')
            return False
        
        text_file = open(yt.get_caption_filepath(), "w", encoding='utf-8')
        text_file.write(en_caption_convert_to_srt)
        text_file.close()

    def process(self, data, inputs, utils):
        start = time.time()

        processes = []
        with ThreadPoolExecutor(max_workers=20) as executor:
            for yt in data:
                processes.append(executor.submit(self.download_captions, yt, utils))       

        end = time.time()
        print(f'took {end-start} seconds')
    
        return data




