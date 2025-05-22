"""
UESimulator.component.systemlogger

관리자용 로그 출력 컴포넌트
"""

import UESimulator.component.err as err
from UESimulator.enums.base import UEIntEnum

class SystemLogger:
    def __init__(self):
        pass

    class ELogLevel(UEIntEnum):
        ERROR = -1
        EVENT = 0
    
    def log(self, level: ELogLevel, content: str):
        output: str = ""
        match level:
            case self.ELogLevel.EVENT:
                output = f"\u001b[1;30m- EVENT \u001b[0;30m{content}\u001b[0m"
            case self.ELogLevel.ERROR:
                output = f"\u001b[1;31m! ERROR \u001b[0;31m{content}\u001b[0m"
        print(output)
    
    def prompt(self, content: str) -> int:
        try:
            val: int = int(input(f"\u001b[1;36m> INPUT \u001b[0;36m{content}\u001b[0m"))
        except ValueError:
            raise err.InvalidInputError
        else:
            return val