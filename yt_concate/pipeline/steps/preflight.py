from pipeline.steps.step import Step
from utils import Utils

class Preflight(Step):
    def process(self, data, inputs, utils):
        print('In Preflight')
        utils.create_dirs()
