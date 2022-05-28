"""Abstract class for Map"""
from abc import ABC, abstractmethod
from typing import Iterable, Tuple


class BaseMap(ABC):
    @abstractmethod
    def __setitem__(self, key: str, value: int) -> None:
        ...

    @abstractmethod
    def __getitem__(self, key: str) -> int:
        ...

    @abstractmethod
    def __delitem__(self, key: str) -> None:
        ...

    @abstractmethod
    def __iter__(self) -> Iterable[Tuple[str, int]]:
        ...

    def __contains__(self, key: str) -> bool:
        for keys, element in self:
            if key == keys:
                return True
        return False

    def __eq__(self, other: 'BaseMap') -> bool:
        if self.__len__() != other.__len__():
            return False
        for zn in self:
            if not other.__contains__(zn[0]):
                return False
            if other[zn[0]] != zn[1]:
                return False
        return True

    def __bool__(self) -> bool:
        if self.__len__() == 0:
            return False
        return True

    @abstractmethod
    def __len__(self):
        ...

    def items(self) -> Iterable[Tuple[str, int]]:
        yield from self

    def values(self) -> Iterable[int]:
        return (item[1] for item in self)

    def keys(self) -> Iterable[str]:
        return (item[0] for item in self)

    @classmethod
    def fromkeys(cls, iterable, value=None) -> 'BaseMap':
        my_class = cls()
        for key in iterable:
            my_class[key] = value
        return iterable

    def update(self, other=None) -> None:
        if other is not None:
            if hasattr(other, 'keys'):
                for key in other.keys():
                    self[key] = other[key]
            else:
                for key, value in other:
                    self[key] = value

    def get(self, key, default=None):
        if self.__contains__(key):
            return self[key]
        return default

    def pop(self, key, *args):
        if not self.__contains__(key):
            if len(args) > 0:
                return args
            raise KeyError
        else:
            znak = self[key]
            self.__delitem__(key)
            return znak

    def popitem(self):
        if self.__len__() == 0:
            raise KeyError
        for zn in self:
            b = zn
        del self[b[0]]
        return b

    def setdefault(self, key, default=None):
        for zn in self:
            if zn[0] == key:
                return zn[1]
        self[key] = default
        return default

    def clear(self):
        for key, value in self:
            del self[key]
        return self

    def write(self, path: str) -> None:
        """write Map in file"""
        with open(path + '/dict.txt', 'w') as file:
            for key, value in self:
                file.write(f" {key}:{value} ")

    @classmethod
    def read(cls, path: str) -> 'BaseMap':
        my_obj = cls()
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                if len(line) != 0:
                    if line != "":
                        line = line.split("\t")
                        my_obj[line[0]] = int(line[1])
        return my_obj

