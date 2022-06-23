
from moviepy.editor import VideoFileClip

from pipeline.steps.step import Step


class EditVideos(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            print(found.time)
            start_time, end_time = self.parse_caption_time(found.time)

            video =  VideoFileClip(found.yt.video_filepath).subclip(start_time, end_time)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break


    def parse_caption_time(self, caption_time):
        start_time, end_time = caption_time.split(' --> ')
        return self.parse_time_str(start_time), self.parse_time_str(end_time)
    
    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000