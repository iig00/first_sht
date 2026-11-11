"""Pyxel application entry and runtime loop."""

import pyxel


class GameApp:
    """Connect Pyxel's runtime to the game update and draw cycle."""

    def __init__(self) -> None:
        pyxel.init(256, 192, title="First Shooting")

    def run(self) -> None:
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        """Update game state once per frame; gameplay is added in later IDs."""

    def draw(self) -> None:
        """Draw the current frame without adding a title screen."""
        pyxel.cls(0)
