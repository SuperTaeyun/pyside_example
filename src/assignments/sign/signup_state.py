from dataclasses import dataclass
import re


@dataclass
class SignupState:
    user_id: str = ""
    password: str = ""
    email: str = ""

    def validate(self) -> dict[str, str]:
        """
        필드 검사 후 유효하지 않은 필드의 {필드명: 에러 메시지} 반환. 종교적인 이유로 정규표현식이 싫어서 AI에게 부탁했다.
        
        :return: {필드명: 에러 메시지}
        """
        errors: dict[str, str] = {}
        # id
        if not re.fullmatch(r"[A-Za-z0-9_]{4,16}", self.user_id):
            errors["user_id"] = "아이디는 영문/숫자/언더스코어 4~16자로 입력하세요."

        # 비밀번호: 8자 이상, 대문자/소문자/숫자 중 2가지 이상 포함 등등
        if len(self.password) < 8:
            errors["password"] = "비밀번호는 8자 이상이어야 합니다."

        # 이메일 형식
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", self.email):
            errors["email"] = "이메일 형식이 올바르지 않습니다."

        return errors
