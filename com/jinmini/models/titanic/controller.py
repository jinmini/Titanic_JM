from com.jinmini.models.titanic.dataset import Dataset
from com.jinmini.models.titanic.service import Service
from icecream import ic

class Controller :
    
    dataset = Dataset() 
    service = Service()

    def modeling(self, train, test):#template method pattern
        this = self.service.preprocess(train, test)
        self.print_this(this)
        #this.train = self.service.create_train(this) #답
        #print("트레인 머신에게 내는 문제")
        #ic(train)
        #this.label = self.service.create_train(this) #survive 제거 - 문제제
        print("트레인")
        #ic(labels)
        return this
    
    def learning(self):
        pass

    def submit(self):
        pass

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. Train 의 type \n {type(this.train)} ')
        print(f'2. Train 의 column \n {this.train.columns} ')
        print(f'3. Train 의 상위 5개 행\n {this.train.head()} ')
        print(f'4. Train 의 null 의 갯수\n {this.train.isnull().sum()}개')
        print(f'5. Test 의 type \n {type(this.test)}')
        print(f'6. Test 의 column \n {this.test.columns}')
        print(f'7. Test 의 상위 1개 행\n {this.test.head()}개')
        print(f'8. Test 의 null 의 갯수\n {this.test.isnull().sum()}개')
        print('*' * 100)