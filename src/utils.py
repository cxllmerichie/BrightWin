import screen_brightness_control as sbc


class Brightness:
    @staticmethod
    def displays() -> list[dict]:
        return sbc.list_monitors_info()

    @staticmethod
    def set(value, display) -> None:
        return sbc.set_brightness(value=value, display=display, no_return=True)

    @staticmethod
    def get(display) -> int:
        return sbc.get_brightness(display=display)[0]
