from pipeline.steps.step import Step


class ReadCaptions(Step):
    # 兩層字典影響易讀性 47-17:30，可再優化
    # 使用pprint查詢字典內容 47-25:42
    # LEC 49: 使用class 替代 雙層字典 

    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                continue
            
            captions = {}
            with open(yt.caption_filepath, 'r', encoding='utf-8') as f:
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
            yt.captions = captions

        return data