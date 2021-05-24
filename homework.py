
class SQL:
    def __init__(self,username,password,sqlname):
        self.Student = {'Liming':[12,180]}
        self.Teacher = {}
        self.flag = 0
        self.username = username
        self.password = password
        self.sqlname = sqlname

    def access(self, host="127.0.0.1", port=8888):
        passwprd = 123
        username = 'root'
        sqlname = ['hzc','stu','tea']


        #判断用户名，密码是否正确
        if self.password == passwprd and self.username == username:
            for i in range(0, len(sqlname)):
                if self.sqlname == sqlname[i]:
                    print('{}:{} is successed!'.format(host, port))
                    self.flag = 1

    def select(self, *args, **kwargs):
        # 判断是否链接数据库
        if not self.flag:
            print('请先连接数据库!')
            exit(-1)

        if args:
            print(args)
            print('!!!')
        if kwargs:
            print(kwargs)
            methods = kwargs['query'].split(',')
            #kwargs['method'].split(',')
            print(methods)
            print('Select {} from {} where {}={}'.format(kwargs['method'], kwargs['query'], kwargs['method'], [kwargs[m] for m in kwargs['method'].split(',')]))





if __name__ == '__main__':
    # p = {'query': 'student', 'method': 'age,name', 'age': '12','name':'li'} # Select name FROM Student where age=12
    sql = SQL('root',123,'hzc')
    sql.access(port=5678)
    sql.select(query='student,teather', method='age,name', age='12', name='LiMing')










