
from moviepy.editor import VideoFileClip
<<<<<<< HEAD
from moviepy.editor import concatenate_videoclips
=======
>>>>>>> aec74c4e7d22e2fbb277888ea757d8b45c1004de

from pipeline.steps.step import Step


class EditVideos(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
<<<<<<< HEAD
=======
            print(found.time)
>>>>>>> aec74c4e7d22e2fbb277888ea757d8b45c1004de
            start_time, end_time = self.parse_caption_time(found.time)

            video =  VideoFileClip(found.yt.video_filepath).subclip(start_time, end_time)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break

<<<<<<< HEAD
        final_clip = concatenate_videoclips(clips)
        outputs_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(outputs_filepath)

=======
>>>>>>> aec74c4e7d22e2fbb277888ea757d8b45c1004de

    def parse_caption_time(self, caption_time):
        start_time, end_time = caption_time.split(' --> ')
        return self.parse_time_str(start_time), self.parse_time_str(end_time)
    
    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000