# 基于 “封装 + 继承 + 多态” 设计「图形计算器」：
# 定义基类 Shape （私有属性 area ，封装计算面积的私有方法 calc_area ）
# 子类 Circle / Rectangle 继承 Shape ，重写面积计算逻辑（多态体现）
# 类变量记录所有图形的创建数量，实例变量存储各自尺寸
# 要求：通过实例调用公开方法获取面积，禁止直接访问私有属性

class Shape:
    count_shape=0
    def __init__(self):
        self._area=0
        Shape.count_shape+=1
    def _calc_area(self):
        raise NotImplementedError("子类必须重写此方法")
    def __str__(self):
        return "图形"
    def get_area(self):
        self._area=self._calc_area()
        return self._area
    @classmethod
    def get_shape_count(cls):
        return cls.count_shape


class Circle(Shape):
    def __init__(self, radius):
        super(Circle, self).__init__()
        self.radius=radius
    def _calc_area(self):
        return 3.14 * self.radius ** 2
    def __str__(self):
        return f"半径为{self.radius}的圆形"


class Rectangle(Shape):
    def __init__(self, width, height):
        super(Rectangle, self).__init__()
        self.width=width
        self.height=height
    def _calc_area(self):
        return self.width * self.height
    def __str__(self):
        return f"宽为{self.width}，长为{self.height}的矩形"


def shape_calculator():
    print("图形计算器\n")

    circle1=Circle(2)
    rectangle1=Rectangle(10,20)
    circle2=Circle(3)

    shapes=[circle1, rectangle1, circle2]
    for shape in shapes:
        print(f"{shape}:面积={shape.get_area()}")

    print(f"\n图形总数：{Shape.get_shape_count()}")

shape_calculator()


# 测试str.strip()
# 测试默认行为：移除空白字符
str1="   hello world   "
str2="\t \nhello world\t\n"
print("原字符1：",str1)
print("处理后字符1：",str1.strip())
print("原字符2：",str2)
print("处理后字符2：",str2.strip())
# 不仅空格会被删除，制表符换行符都会被删除

