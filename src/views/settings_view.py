"""
Settings view — 设置页面
"""
import flet as ft

STATUS_BAR_HEIGHT = 48


def build_settings(
    page: ft.Page,
    gradient_colors,
    text_color,
    text_color2,
    text_color3,
    dark_mode_switch,
    on_back=None,
):
    card_bg = ft.Colors.with_opacity(0.5, "white" if page.theme_mode != ft.ThemeMode.DARK else "0x2A2A2A")
    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Column([
            ft.Container(height=STATUS_BAR_HEIGHT),
            ft.Container(height=8),
            ft.Container(
                padding=ft.padding.Padding(left=8, top=0, right=16, bottom=0),
                content=ft.Row([
                    ft.IconButton(
                        icon=ft.Icons.CHEVRON_LEFT,
                        icon_size=26,
                        icon_color=text_color2(),
                        width=28,
                        height=40,
                        padding=0,
                        on_click=lambda e: on_back() if on_back else None,
                    ),
                    ft.Text("设置", size=16, weight=ft.FontWeight.W_500, color=text_color()),
                ], spacing=0),
            ),
            ft.Container(height=16),
            ft.Container(
                padding=ft.padding.Padding(left=16, top=0, right=16, bottom=0),
                content=ft.Column([
                    ft.Text("通用", size=13, color=text_color3(),
                            weight=ft.FontWeight.W_500),
                    ft.Container(height=8),
                    ft.Container(
                        padding=ft.padding.Padding(left=16, top=12, right=16, bottom=12),
                        border_radius=12,
                        bgcolor=card_bg,
                        content=ft.Column([
                            ft.Container(
                                padding=ft.padding.Padding(left=0, top=0, right=0, bottom=12),
                                content=ft.Row([
                                    ft.Icon(ft.Icons.DARK_MODE, size=22, color="0x4A90D9"),
                                    ft.Container(width=12),
                                    ft.Text("暗黑模式", size=15, color=text_color(), expand=True),
                                    dark_mode_switch,
                                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                            ),
                        ], spacing=0),
                    ),
                ], spacing=0),
            ),
        ], spacing=0, expand=True),
    )
