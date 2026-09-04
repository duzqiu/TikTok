"""Language selection view — 选择语言页面"""
import flet as ft

STATUS_BAR_HEIGHT = 48
PAGE_HORIZONTAL_PADDING = 28

LANGUAGES = [
    "中文简体",
    "中文繁體",
    "English",
    "日本語",
    "한국어",
    "Español",
    "Français",
    "Deutsch",
]


def build_language(page, gradient_colors, text_color, text_color2, text_color3,
                   selected_language, on_back=None, on_select=None):
    card_bg = ft.Colors.with_opacity(
        0.7,
        "0x2A2A2A" if page.theme_mode == ft.ThemeMode.DARK else "white",
    )

    language_rows = []
    for language in LANGUAGES:
        selected = language == selected_language
        language_rows.append(
            ft.Container(
                padding=ft.padding.Padding(left=0, top=14, right=0, bottom=14),
                on_click=lambda e, value=language: on_select(value) if on_select else None,
                content=ft.Row([
                    ft.Text(language, size=15, color=text_color(), expand=True),
                    ft.Icon(
                        ft.Icons.RADIO_BUTTON_CHECKED if selected else ft.Icons.RADIO_BUTTON_UNCHECKED,
                        size=21,
                        color="0x64B5F6" if selected else text_color3(),
                    ),
                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
            )
        )

    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Column([
            ft.Container(height=STATUS_BAR_HEIGHT),
            ft.Container(
                padding=ft.padding.Padding(
                    left=PAGE_HORIZONTAL_PADDING - 8, top=8,
                    right=PAGE_HORIZONTAL_PADDING, bottom=8,
                ),
                content=ft.Row([
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        icon_size=22,
                        icon_color=text_color(),
                        tooltip="返回",
                        on_click=lambda e: on_back() if on_back else None,
                    ),
                    ft.Text("选择语言", size=20, weight=ft.FontWeight.W_500, color=text_color()),
                ], spacing=4),
            ),
            ft.ListView(
                expand=True,
                padding=ft.padding.Padding(left=0, top=8, right=0, bottom=32),
                controls=[
                    ft.Container(
                        margin=ft.margin.Margin(
                            left=PAGE_HORIZONTAL_PADDING, top=0,
                            right=PAGE_HORIZONTAL_PADDING, bottom=0,
                        ),
                        padding=ft.padding.Padding(left=16, top=0, right=16, bottom=0),
                        border_radius=16,
                        bgcolor=card_bg,
                        content=ft.Column(language_rows, spacing=0),
                    ),
                ],
            ),
        ], spacing=0, expand=True),
    )
