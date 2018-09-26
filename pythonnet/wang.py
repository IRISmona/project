# wang.py
class Ren:
    def __init__(self, name):
        self.name = name
        self.xue = 100
        self.qiang = None

    def naqiang(self, qiang):
        if self.qiang == None:
            self.qiang = qiang
            print(self.name, '拿起啦抢')
        else:
            print("you qiang le")

    def anzidan(self, zidan, danjia):
        danjia.baocunzidan(zidan)

    def andanjia(self, qiang, danjia):
        qiang.lianjiedanjia(danjia)

    def kaiqiang(self, diren):
        self.qiang.she(diren)
        print(self.name, '开枪射击了', diren.name)

    def diaoxue(self, shanghaili):
        self.xue -= shanghaili

    def __str__(self):
        return "%s的剩余血量为：%d" % (self.name, self.xue)


class ZiDan:
    def __init__(self, shanghaili):
        self.shanghaili = shanghaili

    def shanghai(self, diren):
        diren.diaoxue(self.shanghaili)


class Qiang:
    def __init__(self):
        self.danjia = None

    def lianjiedanjia(self, danjia):
        if self.danjia == None:
            self.danjia = danjia

    def she(self, diren):
        zidan = self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print("No ZiDan")


class Danjia:
    def __init__(self, rongliang, host):
        self.rongliang = rongliang
        self.ronglianglist = []
        self.host = host

    def baocunzidan(self, zidan):
        if len(self.ronglianglist) < self.rongliang:
            self.ronglianglist.append(zidan)

    def chuzidan(self):
        if len(self.ronglianglist) > 0:
            zidan = self.ronglianglist.pop()
            return zidan
        else:
            return None

    def __str__(self):
        return "%s剩余子弹数量：%d/%d" % (self.host.name, len(self.ronglianglist),
                                   self.rongliang)


# create Mr.Wang
laoWang = Ren("Mr.Wang")
print('有一个人叫',laoWang.name)

# create danjia
danjia = Danjia(20, laoWang)

# While to tianjia zidan
i = 0
while i < 15:
    zidan = ZiDan(5)
    laoWang.anzidan(zidan, danjia)
    i += 1
print(danjia)

# create qiang
print(laoWang.name,'给抢装上弹夹')
qiang = Qiang()
laoWang.andanjia(qiang, danjia)

# create diren
diren = Ren("敌人")
print('出现啦一个敌人', diren)
# 老王拿起枪
laoWang.naqiang(qiang)
# Mr.Wang she diren
laoWang.kaiqiang(diren)
print(diren)
print(danjia)
