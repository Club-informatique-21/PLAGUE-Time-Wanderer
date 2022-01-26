keys = {
    "0": 48,
    "1": 49,
    "2": 50,
    "3": 51,
    "4": 52,
    "5": 53,
    "6": 54,
    "7": 55,
    "8": 56,
    "9": 57,
    "a": 97,

    "AC_BACK": 1073742094,

    "AMPERSAND": 38,
    "ASTERISK": 42,
    "AT": 64,
    "b": 98,
    "BACKQUOTE": 96,
    "BACKSLASH": 92,
    "BACKSPACE": 8,
    "BREAK": 1073741896,
    "c": 99,
    "CAPSLOCK": 1073741881,
    "CARET": 94,
    "CLEAR": 1073741980,
    "COLON": 58,
    "COMMA": 44,
    "CURRENCYSUBUNIT": 1073742005,
    "CURRENCYUNIT": 1073742004,
    "d": 100,
    "DELETE": 127,
    "DOLLAR": 36,
    "DOWN": 1073741905,
    "e": 101,
    "END": 1073741901,
    "EQUALS": 61,
    "ESCAPE": 27,
    "EURO": 1073742004,
    "EXCLAIM": 33,
    "f": 102,
    "F1": 1073741882,
    "F10": 1073741891,
    "F11": 1073741892,
    "F12": 1073741893,
    "F13": 1073741928,
    "F14": 1073741929,
    "F15": 1073741930,
    "F2": 1073741883,
    "F3": 1073741884,
    "F4": 1073741885,
    "F5": 1073741886,
    "F6": 1073741887,
    "F7": 1073741888,
    "F8": 1073741889,
    "F9": 1073741890,
    "g": 103,
    "GREATER": 62,
    "h": 104,
    "HASH": 35,
    "HELP": 1073741941,
    "HOME": 1073741898,
    "i": 105,
    "INSERT": 1073741897,
    "j": 106,
    "k": 107,

    "KP_0": 1073741922,
    "KP_1": 1073741913,
    "KP_2": 1073741914,
    "KP_3": 1073741915,
    "KP_4": 1073741916,
    "KP_5": 1073741917,
    "KP_6": 1073741918,
    "KP_7": 1073741919,
    "KP_8": 1073741920,
    "KP_9": 1073741921,
    "KP_DIVIDE": 1073741908,
    "KP_ENTER": 1073741912,
    "KP_EQUALS": 1073741927,
    "KP_MINUS": 1073741910,
    "KP_MULTIPLY": 1073741909,
    "KP_PERIOD": 1073741923,
    "KP_PLUS": 1073741911,

    "l": 108,
    "LALT": 1073742050,
    "LCTRL": 1073742048,
    "LEFT": 1073741904,
    "LEFTBRACKET": 91,
    "LEFTPAREN": 40,
    "LESS": 60,
    "LGUI": 1073742051,
    "LMETA": 1073742051,
    "LSHIFT": 1073742049,
    "LSUPER": 1073742051,
    "m": 109,
    "MENU": 1073741942,
    "MINUS": 45,
    "MODE": 1073742081,
    "n": 110,
    "NUMLOCK": 1073741907,
    "NUMLOCKCLEAR": 1073741907,
    "o": 111,
    "p": 112,
    "PAGEDOWN": 1073741902,
    "PAGEUP": 1073741899,
    "PAUSE": 1073741896,
    "PERCENT": 37,
    "PERIOD": 46,
    "PLUS": 43,
    "POWER": 1073741926,
    "PRINT": 1073741894,
    "PRINTSCREEN": 1073741894,
    "q": 113,
    "QUESTION": 63,
    "QUOTE": 39,
    "QUOTEDBL": 34,
    "r": 114,
    "RALT": 1073742054,
    "RCTRL": 1073742052,
    "RETURN": 13,
    "RGUI": 1073742055,
    "RIGHT": 1073741903,
    "RIGHTBRACKET": 93,
    "RIGHTPAREN": 41,
    "RMETA": 1073742055,
    "RSHIFT": 1073742053,
    "RSUPER": 1073742055,
    "s": 115,
    "SCROLLLOCK": 1073741895,
    "SCROLLOCK": 1073741895,
    "SEMICOLON": 59,
    "SLASH": 47,
    "SPACE": 32,
    "SYSREQ": 1073741978,
    "t": 116,
    "TAB": 9,
    "u": 117,
    "UNDERSCORE": 95,
    "UNKNOWN": 0,
    "UP": 1073741906,
    "v": 118,
    "w": 119,
    "x": 120,
    "y": 121,
    "z": 122,
}


def get_key(name: str = "UNKNOWN"):
    try:
        return keys[name]
    except KeyError:
        return 0

def get_key_name(id: int = 0):
    for key_name, ID in keys:
        if ID == id:
            return key_name
    return 0
