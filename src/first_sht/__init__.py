"""A small shooting game using only Python's standard library."""

import random
import time
import tkinter as tk

WIDTH, HEIGHT = 640, 720


class Game:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("First Shooting")
        root.resizable(False, False)
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                                bg="#091323", highlightthickness=0)
        self.canvas.pack()
        self.keys: set[str] = set()
        root.bind("<KeyPress>", self.press)
        root.bind("<KeyRelease>", lambda e: self.keys.discard(e.keysym.lower()))
        root.bind("<FocusOut>", lambda _: self.keys.clear())
        self.reset()
        self.last_time = time.monotonic()
        self.tick()

    def reset(self) -> None:
        self.canvas.delete("all")
        self.keys.clear()
        self.score = 0
        self.lives = 3
        self.over = False
        self.cooldown = 0.0
        self.spawn_timer = 0.5
        self.bullets: list[int] = []
        self.enemies: dict[int, float] = {}
        for _ in range(65):
            x, y = random.randrange(WIDTH), random.randrange(HEIGHT)
            self.canvas.create_oval(x, y, x + 2, y + 2, fill="#405573", outline="")
        self.player = self.canvas.create_polygon(
            320, 640, 300, 680, 320, 670, 340, 680,
            fill="#62e8f5", outline="#c4fcff", width=2)
        self.hud = self.canvas.create_text(20, 24, anchor="w", fill="white",
                                          font=("Arial", 16, "bold"))
        self.canvas.create_text(WIDTH / 2, HEIGHT - 18, fill="#9cafca",
                                text="Move: Left / Right or A / D     Shoot: Space     Restart: R")
        self.update_hud()

    def press(self, event: tk.Event) -> None:
        key = event.keysym.lower()
        self.keys.add(key)
        if key == "r" and self.over:
            self.reset()

    def update_hud(self) -> None:
        self.canvas.itemconfigure(self.hud, text=f"SCORE  {self.score:05d}     LIFE  {self.lives}")

    def lose_life(self) -> None:
        self.lives -= 1
        self.update_hud()
        if self.lives <= 0:
            self.over = True
            self.canvas.create_rectangle(100, 275, 540, 420, fill="#15243d", outline="#62e8f5")
            self.canvas.create_text(320, 320, text="GAME OVER", fill="white",
                                    font=("Arial", 32, "bold"))
            self.canvas.create_text(320, 375, text=f"Score: {self.score}    |    Press R to restart",
                                    fill="#62e8f5", font=("Arial", 16))

    def step(self, dt: float) -> None:
        direction = int(bool(self.keys & {"right", "d"})) - int(bool(self.keys & {"left", "a"}))
        bounds = self.canvas.bbox(self.player)
        if bounds:
            dx = max(4 - bounds[0], min(direction * 360 * dt, WIDTH - 4 - bounds[2]))
            self.canvas.move(self.player, dx, 0)
        self.cooldown -= dt
        if "space" in self.keys and self.cooldown <= 0:
            x, y = self.canvas.coords(self.player)[:2]
            self.bullets.append(self.canvas.create_rectangle(x - 3, y - 16, x + 3, y,
                                                             fill="#ffdf75", outline=""))
            self.cooldown = 0.18
        self.spawn_timer -= dt
        if self.spawn_timer <= 0:
            x = random.randint(26, WIDTH - 26)
            enemy = self.canvas.create_oval(x - 18, -40, x + 18, -4,
                                            fill="#fa697d", outline="#ffb7c1", width=2)
            self.enemies[enemy] = random.uniform(95, 155) + min(self.score * 0.12, 180)
            self.spawn_timer = max(0.22, 0.85 - self.score / 1800)
        for bullet in self.bullets[:]:
            self.canvas.move(bullet, 0, -560 * dt)
            box = self.canvas.bbox(bullet)
            if box is None or box[3] < 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)
                continue
            hit = next((item for item in self.canvas.find_overlapping(*box)
                        if item in self.enemies), None)
            if hit is not None:
                self.canvas.delete(hit, bullet)
                del self.enemies[hit]
                self.bullets.remove(bullet)
                self.score += 10
                self.update_hud()
        for enemy, speed in list(self.enemies.items()):
            self.canvas.move(enemy, 0, speed * dt)
            box = self.canvas.bbox(enemy)
            if box and (box[1] > HEIGHT or self.player in self.canvas.find_overlapping(*box)):
                self.canvas.delete(enemy)
                del self.enemies[enemy]
                self.lose_life()
                if self.over:
                    return

    def tick(self) -> None:
        now = time.monotonic()
        dt = min(now - self.last_time, 0.05)
        self.last_time = now
        if not self.over:
            self.step(dt)
        self.root.after(16, self.tick)


def main() -> None:
    root = tk.Tk()
    Game(root)
    root.mainloop()
