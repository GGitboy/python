#!/usr/bin/python 
#获取命令行选项后的文件路径 
import sys
import csv
from collections import namedtuple  #collections模块中的 nametuple类
#命名元祖  可以通过属性名,索引，迭代 访问数据
IncomeTaxQuickLookupItem = namedtuple(
'IncomeTaxQuickLookupItem',
['start_point','tax_rate','quick_subtractor']   #属性名称
)
INCOME_TAX_START_POINT = 3500 #个税起征点
# 在列表中存入命名元祖

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(35000,0.30,2755),
    IncomeTaxQuickLookupItem(55000,0.35,5505),
    IncomeTaxQuickLookupItem(9000,0.25,1005),
    IncomeTaxQuickLookupItem(4500,0.2,555),
    IncomeTaxQuickLookupItem(1500,0.1,105),
    IncomeTaxQuickLookupItem(0,0.03,0),
]

class Args(object):
    def __init__(self):
        self.argv = sys.argv[1:]

    def _get_value_after_option(self,option):
        try:
            index = self.argv.index(option) #获得列表中各个选项
            return self.argv[index + 1]
        except (ValueError,IndexError):
            print('Parameter Error')
            exit()

    @property #  把类的方法定义为属性  变为属性的时候调用不需要加() 
    def config_path(self):
        return self._get_value_after_option('-c')

    @property
    def userdata_path(self):
        return self._get_value_after_option('-d')

    @property
    def output_path(self):
        return self._get_value_after_option('-o')

args = Args() 
print (args.config_path)
print (args.userdata_path)
print (args.output_path)


class Config(object):

    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):# 配置方法返回配置文件中的数据 
        config_path = args.config_path
        config = {}
        with open(config_path)as f:
            for line in f.readlines():
                key,value = line.strip().split(' = ')  # stip()函数 ，split()函数 注意split中分隔符的书写
                try:
                    config[key] = float(value)
                except VlaueError:
                    print('Parameter Error')
                    exit()
#        print(config)  # 输出配置文件中的内容
        return config

    def _get_config(self,key):#配置方法获得 键对应的值                    
        
        try:
            return self.config[key]
        except keyError:
            print('Config Error')
            exit()

    @property
    def social_insurance_baseline_low(self): # 返回最低基数
        return self._get_config('JiShuL')

    @property
    def social_insurance_baseline_high(self): #返回最高基数
        return self._get_config('JiShuH')

    @property
    def social_insurance_total_rate(self): # sum 函数  返回社保总和
        return sum([
        self._get_config('YangLao'),
        self._get_config('YiLiao'), 
        self._get_config('ShiYe'), 
        self._get_config('GongShang'), 
        self._get_config('ShengYu'), 
        self._get_config('GongJiJin'), 
        ])


config = Config()

#print(config.config)
#print(config._get_config('JiShuL'))


class Userdata(object):
    def __init__(self):
        self.userdata = self._get_data()  #将实例方法赋值给实例变量

    def _get_data(self):
        userdata_path = args.userdata_path
        userdata = []
        with open(userdata_path) as f:
            for line in f.readlines():
                user_id,user_salary = line.strip().split(',') #这样的赋值还是想不到的
                try:
                    income = int(user_salary)
                except ValueError:
                    print('Parameter Error')
                    exit()
                userdata.append((user_id,income)) # 这里用2个圆括号
        return userdata                    

    def __iter__(self):
        return iter(self.userdata)  #  生成迭代器 (不太明白)
                

#userdata=Userdata()

#print(userdata.userdata)


class IncomeTaxCalculator(object):
    
    def __init__(self,userdata):
        self.userdata = userdata

    @staticmethod  #使用类的静态方法
    def calc_social_insurance_money(income): #计算社会保险金
        if income < config.social_insurance_baseline_low:
            return config.social_insurance_baseline_low * \
            config.social_insurance_total_rate
        if income > config.social_insurance_baseline_low:
            return config.social_insurance_baseline_high * \
            config.social_insurance_total_rate
        return income* config.social_insurance_total_rate


    @classmethod  # 定义一个类方法
    def calc_income_tax_and_remain(cls,income): # 计算应纳金额和税后工资
        social_insurance_money = cls.calc_social_insurance_money(income)
        real_income = income - social_insurance_money  #实际收入
        taxable_part = real_income - INCOME_TAX_START_POINT  #应纳税所得额
        if taxable_part <= 0:
            return '0.00' ,'{:.2f}'.format(real_income)
        for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
            if taxable_part > item.start_point:
                tax = taxable_part * item.tax_rate - item.quick_subtractor # 应纳税额
                return '{:.2f}'.format(tax),'{:.2f}'.format(real_income -tax)

    def calc_for_all_userdata(self): # 获得用户的数据
        result = []

        for user_id,income in self.userdata:
            data = [user_id,income]
            social_insurance_money = '{:.2f}'.format(self.calc_social_insurance_money(income)) 
#社保金额
            tax,remain = self.calc_income_tax_and_remain(income)
#应纳税额和税后工资
            data += [social_insurance_money,tax,remain]
#
            result.append(data)
        return result

    def export(self,default ='csv'):  # 以csv 方式写入数据

        result = self.calc_for_all_userdata()
        with open(args.output_path,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

if __name__ == '__main__':
    calculator = IncomeTaxCalculator(Userdata())
    calculator.export()
