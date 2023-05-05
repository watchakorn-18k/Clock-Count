import flet as ft
import tkinter as tk
import asyncio
import os

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


class Countdown(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.seconds = 0

    async def did_mount_async(self):
        self.running = True
        self.task = asyncio.create_task(self.update_timer())
        self.task.cancel()

    async def will_unmount_async(self):
        self.running = False

    def stop(self):
        self.task.cancel()

    def start(self):
        self.task = asyncio.create_task(self.update_timer())

    def restart(self):
        self.task.cancel()
        self.seconds = 0
        self.task = asyncio.create_task(self.update_timer())

    async def update_timer(self):
        while self.running:
            print(self.running)
            await asyncio.sleep(1)
            self.seconds += 1
            self.minutes = self.seconds // 60
            self.hours = self.minutes // 60
            self.minutes_left = self.minutes % 60
            self.seconds_left = self.seconds % 60
            self.timer_display.value = (
                f"{self.hours:02d}:{self.minutes_left:02d}:{self.seconds_left:02d}"
            )
            await self.update_async()

    def build(self):
        self.timer_display = ft.Text("0.00.00", size=60)
        return self.timer_display


async def main(page: ft.page):
    clock_count = Countdown()

    def quits(e):
        pid = os.getpid()
        os.system(f"taskkill /pid {pid} /f /t")

    async def minimize(e):
        page.window_minimized = True
        await page.update_async()

    page.title = "Clock-Count ⏰ จับเวลาสอน wk-18k"
    page.window_height = int(screen_height * 0.25)  # reduce to 20%
    page.window_width = int(screen_width * 0.2)  # reduce to 20%
    page.window_resizable = False
    page.window_top = (70.0 / 100) * screen_height
    page.window_left = (79.8 / 100) * screen_width
    page.window_frameless = True
    page.theme = ft.Theme(font_family="Kanit")
    page.dark_theme = ft.Theme(font_family="Kanit")
    print(page.window_minimized)
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.LOCK_CLOCK),
        leading_width=40,
        title=ft.Text("Clock Count จับเวลาสอน wk 18k", size=15),
        center_title=False,
        bgcolor=ft.colors.TRANSPARENT,
        actions=[
            ft.Container(
                content=ft.Row(
                    [
                        ft.IconButton(ft.icons.MINIMIZE, on_click=minimize),
                        ft.IconButton(ft.icons.CLOSE, on_click=quits),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                padding=5,
            )
        ],
    )

    await page.add_async(
        ft.Container(
            content=ft.Column(
                [
                    ft.Column(
                        [
                            ft.Row(
                                [clock_count],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [
                                    ft.TextButton(
                                        "เริ่ม",
                                        on_click=lambda x: clock_count.start(),
                                    ),
                                    ft.TextButton(
                                        "หยุด",
                                        on_click=lambda x: clock_count.stop(),
                                    ),
                                    ft.IconButton(
                                        ft.icons.REFRESH,
                                        on_click=lambda x: clock_count.restart(),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                ],
            )
        )
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    await page.update_async()


if __name__ == "__main__":
    ft.app(target=main)
