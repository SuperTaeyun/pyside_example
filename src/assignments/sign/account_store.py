from src.assignments.sign.signup_state import SignupState


class AccountStore:

    def __init__(self):
        self._accounts: dict[str, SignupState] = {}

    def add_account(self, state: SignupState) -> None:
        """
        Account 추가.아이디 중복 고려하지 않음.
        """
        self._accounts[state.user_id] = SignupState(
            user_id=state.user_id,
            password=state.password,
            email=state.email
        )
        print(f"add_count: user_id:{state.user_id}, password:{state.password}")

    def is_exists(self, user_id: str, password: str) -> bool:
        user = self._accounts.get(user_id)
        return user is not None and user.password == password
