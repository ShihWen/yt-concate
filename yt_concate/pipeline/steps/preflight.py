from pipeline.steps.step import Step
from utils import Utils

class Preflight(Step):
    print('In Preflight')
    Utils.create_dirs()
