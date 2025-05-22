"""
UESimulator.component.err

커스텀 Exception 클래스들 정의
"""

class UEError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self._message: str = message
    
    @property
    def message(self):
        return self._message

class InvalidInputError(UEError):
    def __init__(self):
        super().__init__("잘못된 입력 형식입니다.")

class FileNotFoundError(UEError):
    def __init__(self):
        super().__init__("파일을 여는 데 실패했습니다. data 폴더의 경로를 확인해 주세요.")

class RaceNotFoundError(UEError):
    def __init__(self):
        super().__init__("입력된 레이스 ID와 일치하는 레이스를 찾지 못했습니다.")
        
class SimulationInitFailError(UEError):
    def __init__(self):
        super().__init__("시뮬레이션 준비에 실패했습니다.")