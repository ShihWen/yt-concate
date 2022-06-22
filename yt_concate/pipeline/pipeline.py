from pipeline.steps.step import StepException

'''
任何步驟皆需要return東西(交接)data給下一步驟
不然會出錯
參考lec 49-13:00

'''

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)

            except StepException as e:
                print("exception happened in step", e)
                break