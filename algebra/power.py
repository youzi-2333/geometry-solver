"""
表示幂的数据类。
"""

from numbers import Rational
from typing import Union


class Unknown:
    """
    未知数。
    """

    _character: str

    @property
    def character(self) -> str:
        """字母。"""
        return self._character

    def __init__(self, character: str):
        if not character.isalpha():
            raise ValueError(f"character must be a letter ({character})")
        self._character = character[0]

    def __repr__(self):
        return f"Unknown({self._character!r})"


class Power:
    """
    幂。
    """

    def __init__(
        self,
        base: Union[Rational, "Power", Unknown],
        exponent: Union[Rational, "Power", Unknown],
    ):
        # 能求值的全部求值
        self.base = base
        self.exponent = exponent
        self.solve()

    def __repr__(self):
        return f"Power({self.base!r}, {self.exponent!r})"

    def solve(self) -> Union[Rational, "Power"]:
        """
        对自身尽量求值并返回。
        """
        if isinstance(self.base, Rational) and isinstance(self.exponent, Rational):
            return self.base**self.exponent
        if isinstance(self.base, Power):
            self.base = self.base.solve()
        if isinstance(self.exponent, Power):
            self.exponent = self.exponent.solve()
        return self

    def simplify(self):
        """
        化简。
        """
        if isinstance(self.base, Power):
            self.base = self.base.solve()
        if isinstance(self.exponent, Power):
            self.exponent = self.exponent.solve()
