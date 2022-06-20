from settings import DOWNLOADS_DIR
from settings import CAPTIONS_DIR
from settings import VIDEOS_DIR



class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_video_id_from_url(url):
        return url.splits('watch?v=')[-1]


    def get_caption_path(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url) + '.txt')