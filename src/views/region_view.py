"""Region selection view — 选择地区页面"""
import flet as ft

STATUS_BAR_HEIGHT = 48
PAGE_HORIZONTAL_PADDING = 28

REGIONS = [
    ("🇨🇳", "中国"),
    ("🇺🇸", "美国"),
    ("🇬🇧", "英国"),
    ("🇯🇵", "日本"),
    ("🇰🇷", "韩国"),
    ("🇸🇬", "新加坡"),
    ("🇨🇦", "加拿大"),
    ("🇦🇺", "澳大利亚"),
]


def build_region(page, gradient_colors, text_color, text_color2, text_color3,
                 selected_region, on_back=None, on_select=None):
    card_bg = ft.Colors.with_opacity(
        0.7,
        "0x2A2A2A" if page.theme_mode == ft.ThemeMode.DARK else "white",
    )

    region_rows = []
    for flag, region in REGIONS:
        selected = region == selected_region
        region_rows.append(
            ft.Container(
                padding=ft.padding.Padding(left=0, top=14, right=0, bottom=14),
                on_click=lambda e, value=region: on_select(value) if on_select else None,
                content=ft.Row([
                    ft.Text(flag, size=22),
                    ft.Container(width=12),
                    ft.Text(region, size=15, color=text_color(), expand=True),
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
                        icon=ft.Icons.CHEVRON_LEFT,
                        icon_size=26,
                        icon_color=text_color2(),
                        width=28,
                        height=40,
                        padding=0,
                        tooltip="返回",
                        on_click=lambda e: on_back() if on_back else None,
                    ),
                    ft.Text("选择地区", size=16, weight=ft.FontWeight.W_500, color=text_color()),
                ], spacing=0),
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
                        content=ft.Column(region_rows, spacing=0),
                    ),
                ],
            ),
        ], spacing=0, expand=True),
    )
