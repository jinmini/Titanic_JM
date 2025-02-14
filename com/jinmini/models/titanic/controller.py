from com.jinmini.models.titanic.dataset import Dataset
from com.jinmini.models.titanic.service import Service

class Controller :
    
    dataset = Dataset() 
    service = Service()

    def modeling(self, train):
        this = self.dataset 
        this.train = self.service.new_model(train)
        print("트레인 데이터")
        print(this.train)
        return this
