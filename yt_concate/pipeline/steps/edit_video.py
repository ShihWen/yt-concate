
from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from pipeline.steps.step import Step


class EditVideos(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            start_time, end_time = self.parse_caption_time(found.time)

            video_duration = VideoFileClip(found.yt.video_filepath).duration
            start_time_sec = self.parse_time_to_sec(start_time)
            end_time_sec = self.parse_time_to_sec(end_time)

            # print(found.yt.url ,video_duration, start_time_sec, end_time_sec)
            if start_time_sec > video_duration or end_time_sec > video_duration:
                print(f'caption_timeline missmatch with video duration: {found.yt.url}')
                continue

            video =  VideoFileClip(found.yt.video_filepath).subclip(start_time, end_time)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break

        final_clip = concatenate_videoclips(clips)
        outputs_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(outputs_filepath)


    def parse_caption_time(self, caption_time):
        start_time, end_time = caption_time.split(' --> ')
        return self.parse_time_str(start_time), self.parse_time_str(end_time)
    
    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000

    def parse_time_to_sec(self, tuple_time):
        hr_to_sec = tuple_time[0] * 60 * 60
        min_to_sec = tuple_time[1] * 60
        sec = tuple_time[2]
        return hr_to_sec + min_to_sec + sec
