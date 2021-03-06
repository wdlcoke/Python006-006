
class Animal():

    def __init__(self, animal_type, somatotype, nature):
        '''
        动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
        类型 ：食肉 、 食素、 杂食
        体型 ：大型 、 中等、 小型
        性格 ：温顺 、 中性、 凶猛
        '''
        self.animal_type = animal_type  
        self.somatotype = somatotype
        self.nature = nature

    @property
    def ls_fierce(self):
        return True if self.animal_type == '食肉' and (self.somatotype == '中等' or self.somatotype == '大型') and self.nature == '凶猛' else False


class Cat(Animal):

    sound = '喵喵喵。。。'

    def __init__(self, name ,animal_type, somatotype, nature):
        super().__init__(animal_type, somatotype, nature)
        self.name = name 

    @property
    def is_pet(self):
        return False if self.ls_fierce else True
        


class Dog(Animal):
    sound = '汪汪汪。。。'

    def __init__(self, name ,animal_type, somatotype, nature):
        super().__init__(animal_type, somatotype, nature)
        self.name = name 

    @property
    def is_pet(self):
        return False if self.ls_fierce else True

class Zoo(object):
    

    def __init__(self,name):
        self.name = name 
        self.__animals = dict()
    
    def add_animal(self, animal):
        animal_name = animal.__class__.__name__

        if animal_name in self.__animals:

            print(f"【{animal_name}】--【{animal.name}】已存在，请勿重复添加~")

        else:
            self.__animals[animal_name] = animal


if __name__ == '__main__':


    '''
    实例化动物园
    z = Zoo('时间动物园')
    实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    增加一只猫到动物园
    z.add_animal(cat1)
    动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')

    '''

    # 实例化动物园
    z = Zoo('时间动物园')

    # 实例化两只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫1', '食肉', '小', '温顺')

    # 增加1只猫到动物园
    z.add_animal(cat1)

    # 动物园是否有猫这种动物
    has_cat = hasattr(z, 'Cat')
