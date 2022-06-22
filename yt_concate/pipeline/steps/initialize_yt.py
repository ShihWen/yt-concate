from pipeline.steps.step import Step
from model.yt import YT

'''
LEC 48
1. 由於ReadCaption()下的Process()程式碼使用雙階層字典，其劣勢有:
    - 可讀性較差，使用上需要額外花時間理解
    - 使用時需要喜code重新組裝相關路經
   
2. 使用class進行優化程
'''

class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]
