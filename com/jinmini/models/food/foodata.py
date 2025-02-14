from dataclasses import dataclass

class Dataset:
    food : object 
    food_test : object 
    context : str
    fname : str
    id : str
    label : str

    @property
    def food(self) -> object:
        return self._food
    
    @food.setter
    def food(self, food):
        self._food = food
    
    @property
    def food_test(self) -> object:
        return self._food_test
    
    @food_test.setter
    def food_test(self, food_test):
        food_test._train = food_test
    
    @property
    def context(self) -> str:
        return self._context
    
    @context.setter
    def context(self, context):
        self._context = context
    
    @property
    def fname(self) -> str:
        return self._fname
    
    @fname.setter
    def fname(self, fname):
        self._fname = fname
    
    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def label(self) -> str:
        return self._label
    
    @label.setter
    def label(self, label):
        self._label = label
    