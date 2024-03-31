"""
程序入口点。
"""

from algebra.power import Power, Unknown
import sympy


def main():
    """主函数。"""
    print(Power(Power(2, 0.5), 2))


if __name__ == "__main__":
    main()
