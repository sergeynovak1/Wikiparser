class Integer():
    def __init__(self, number):
        self.number = number
        if number < 0:
            a = '-'
        else:
            a = '+'
        x = abs(number)
        d = dict()
        i = 0
        while x > 0:
            d[i] = x%10
            x = x//10
            i += 1
        d['znak'] = a
        self.dict = d

    def __add__(self, other):
        if self.dict['znak'] != other.dict['znak']:
            if self.dict['znak'] == '-':
                self.dict['znak'] = '+'
                c = Integer(0)
                c = other - self
                return c
            else:
                other.dict['znak'] = '+'
                c = Integer(0)
                c = self - other
                return c
        if len(self.dict) > len(other.dict):
            lenght = len(self.dict)
        else:
            lenght = len(other.dict)
        c = Integer(0)
        for i in range(lenght-1):
            c.dict[i] = 0
            if i in self.dict:
                c.dict[i] += self.dict[i]
            if i in other.dict:
                c.dict[i] += other.dict[i]
        for i in range(lenght-1):
            if c.dict[i] >= 10:
                c.dict[i] -= 10
                if (i+1) not in c.dict:
                    c.dict[i+1] = 0
                c.dict[i+1] += 1
        c.dict['znak'] = self.dict['znak']

        x = 0
        for i in range(len(c.dict)-2, -1, -1):
            x = x*10 + c.dict[i]
        if c.dict['znak'] == '-':
            x *= -1

        return x

    def __sub__(self, other):
        if self.dict['znak'] != other.dict['znak']:
            if self.dict['znak'] == '-':
                other.dict['znak'] = '-'
                c = Integer(0)
                c = other + self
                return c
            else:
                other.dict['znak'] = '+'
                c = Integer(0)
                c = other + self
                return c
        if len(self.dict) > len(other.dict):
            lenght = len(self.dict)
        else:
            lenght = len(other.dict)
        c = Integer(0)
        for i in range(lenght-1):
            c.dict[i] = 0
            if i in self.dict and i in other.dict:
                c.dict[i] = self.dict[i] - other.dict[i]
            elif self.dict[i]:
                c.dict[i] = self.dict[i]
            elif other.dict[i]:
                c.dict[i] = other.dict[i]
        for i in range(lenght-1):
            if c.dict[i] < 0:
                c.dict[i] += 10
                if (i+1) not in c.dict:
                    c.dict[i+1] = 0
                c.dict[i+1] -= 1

        x = 0
        for i in range(len(c.dict) - 2, -1, -1):
            x = x * 10 + c.dict[i]
        if c.dict['znak'] == '-':
            x *= -1

        return x

    def __neg__(self):
        c = Integer(0)
        c.dict = self.dict
        if c.dict['znak'] == '-':
            c.dict['znak'] = '+'
        else:
            c.dict['znak'] = '-'

        x = 0
        for i in range(len(c.dict) - 2, -1, -1):
            x = x * 10 + c.dict[i]
        if c.dict['znak'] == '-':
            x *= -1

        return x

    def __eq__(self, other):
        c = self - other
        return c == 0

    def __ne__(self, other):
        c = self - other
        return c != 0

    def __lt__(self, other):
        c = self - other
        return c < 0

    def __le__(self, other):
        c = self - other
        return c <= 0

    def __gt__(self, other):
        c = self - other
        return c > 0

    def __ge__(self, other):
        c = self - other
        return c >= 0

    def __repr__(self):
        return repr(self.number)

    def __str__(self):
        return str(self.number)



