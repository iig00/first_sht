"""Tests for the I-01 Pyxel runtime wiring."""

import unittest
from unittest.mock import patch

import main
from game.app import GameApp


class GameAppRuntimeTests(unittest.TestCase):
    def test_initializes_pyxel_window(self) -> None:
        with patch("game.app.pyxel.init") as init:
            GameApp()

        init.assert_called_once_with(256, 192, title="First Shooting")

    def test_run_connects_update_and_draw_callbacks(self) -> None:
        with patch("game.app.pyxel.init"), patch("game.app.pyxel.run") as run:
            app = GameApp()
            app.run()

        run.assert_called_once_with(app.update, app.draw)

    def test_draw_clears_screen(self) -> None:
        with patch("game.app.pyxel.init"), patch("game.app.pyxel.cls") as clear:
            app = GameApp()
            app.draw()

        clear.assert_called_once_with(0)

    def test_main_constructs_and_runs_game_app(self) -> None:
        with patch("main.GameApp") as game_app:
            main.main()

        game_app.assert_called_once_with()
        game_app.return_value.run.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
