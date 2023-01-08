import screen_brightness_control as sbc


class Controls:
    def __init__(self):
        self.displays = sbc.list_monitors_info()

    @staticmethod
    def set(value, display) -> None:
        return sbc.set_brightness(value=value, display=display)

    @staticmethod
    def get(display) -> int:
        return sbc.get_brightness(display=display)[0]
