from pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('In Postflight')
        utils.delete_cap_files()
        # utils.delete_video_files()