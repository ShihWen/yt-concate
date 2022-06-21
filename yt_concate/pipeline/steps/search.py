from pipeline.steps.step import Step

class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']