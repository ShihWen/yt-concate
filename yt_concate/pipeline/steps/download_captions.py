from pytube import YouTube
import os
import time

from pipeline.steps.step import Step
from pipeline.steps.step import StepException



class DownloadCaptions(Step):
    def __init__(self):
        pass

    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print(f'downloading captions for {yt.id}')
            if utils.caption_file_exists(yt):
                print(f'file exists: {yt.url}')
                continue
            
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt =(en_caption.generate_srt_captions())

            except (KeyError, AttributeError) as e:
                print(f'Error when downloading caption for {yt.url}')
                continue
            
            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        #print(f'took {end-start} seconds')
    
        return data




