import json
import os

CELL   = 20
COLS   = 30
ROWS   = 22        
HUD_H  = 40         
FIELD_Y = HUD_H     
WIDTH  = COLS * CELL         
HEIGHT = HUD_H + ROWS * CELL 

FOOD_LIFETIME_MS    = 5000
POWERUP_LIFETIME_MS = 8000
POWERUP_EFFECT_MS   = 5000

SETTINGS_FILE = "settings.json"

BLACK      = (18, 18, 24)
WHITE      = (245, 245, 245)
GREEN      = (52, 168, 83)
DARK_GREEN = (29, 110, 55)
RED        = (230, 72, 72)
ORANGE     = (255, 170, 40)
PURPLE     = (157, 78, 221)
GRAY       = (60, 60, 70)
DARK_RED   = (120, 20, 20)
CYAN       = (0, 210, 230)
BLUE       = (60, 100, 220)
YELLOW     = (255, 215, 0)
WALL_COLOR = (90, 90, 110)
BG_PANEL   = (28, 28, 38)
ACCENT     = (52, 168, 83)
DIM        = (100, 100, 120)

FOODS = [(1, RED), (2, ORANGE), (3, PURPLE)]

POWERUP_TYPES = {
    "speed":  {"color": CYAN,   "symbol": ">>"},
    "slow":   {"color": BLUE,   "symbol": "<<"},
    "shield": {"color": YELLOW, "symbol": "[]"},
}

DEFAULT_SETTINGS = {
    "snake_color": [52, 168, 83],
    "grid_overlay": True,
    "sound": True,
}


def load_settings() -> dict:
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE) as f:
                data = json.load(f)
            for k, v in DEFAULT_SETTINGS.items():
                data.setdefault(k, v)
            return data
        except Exception:
            pass
    return dict(DEFAULT_SETTINGS)


def save_settings(settings: dict) -> None:
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)