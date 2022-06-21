from pprint import pprint
import os

from pipeline.steps.step import Step
from settings import CAPTIONS_DIR

class ReadCaptions(Step):
    # 兩層字典影響易讀性 47-17:30，可再優化
    # 使用pprint查詢字典內容 47-25:42

    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r', encoding='utf-8') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:
                        caption = line
                        captions[caption] = time
                        time_line = False
            data[caption_file] = captions

        #pprint(data)
        return data