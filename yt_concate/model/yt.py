from settings import CAPTIONS_DIR
from settings import VIDEOS_DIR
import os


'''
1. 如何在YT中使用Utils裡的method?
    - 建立utils實例並使用之 
        -> 每個url都建一次utils，與main()設計理念不符
           (即建一個大家傳遞使用節省記憶體)
    - 將 utils 中的method 改寫為 class method/static method
        -> 改寫耗時、如果utils之中有不能改寫成class method/static method
           ，將整組不能用   
    - 將 utils 當參數傳入 YT
        -> 傳入的參數通常為該物件的屬性，utils不算YT的屬性
        -> 參數越少越好
    - 將utils中與YT相關的function搬到YT中(即與影片相關之各種function)


'''

class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url(self.url)
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_filepath()
        self.captions = None

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]
    

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

     
    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + '.txt')


    def __str__(self):
          return '<YT(' + str(self.id) + ')>'

    
    def __repr__(self):
        content = ' : '.join([
            'id=' + str(self.id),
            'caption_filepath=' + str(self.caption_filepath),
            'video_filepath=' + str(self.video_filepath)
        ])
        return '<YT(' + content +   ')>'
