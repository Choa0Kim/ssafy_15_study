class Counter:
    def increment(self):
        self.count += 1

    # 인스턴스 메서드


c1 = Counter()
c2 = Counter()
# 인스턴스 메서드 호출
print(c1.count) #0
c1.increment()
print(c1.count)#1
