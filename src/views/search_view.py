"""
Search view - 独立搜索页面
"""
import flet as ft


STATUS_BAR_HEIGHT = 48


def build_search(page: ft.Page, gradient_colors, text_color, text_color2, on_back):
    hot_words = [
        "iPhone 17", "AI大模型", "新能源汽车", "世界杯",
        "秋季穿搭", "电影推荐", "健康饮食", "旅行攻略",
    ]
    search_field = ft.TextField(
        hint_text="搜索内容、用户或话题",
        border_radius=12,
        border_color="0xE0E0E0",
        focused_border_color="0x4A90D9",
        text_size=13,
        expand=True,
        content_padding=ft.padding.Padding(left=12, top=2, right=12, bottom=2),
    )

    hot_chips = ft.Row(spacing=8, wrap=True)
    for word in hot_words:
        hot_chips.controls.append(
            ft.Container(
                padding=ft.padding.Padding(left=12, top=6, right=12, bottom=6),
                border_radius=16,
                bgcolor=ft.Colors.with_opacity(0.1, "0x4A90D9"),
                content=ft.Text(word, size=12, color="0x4A90D9"),
            )
        )

    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Column(
            [
                ft.Container(height=STATUS_BAR_HEIGHT),
                ft.Container(
                    height=48,
                    padding=ft.padding.Padding(left=8, top=0, right=12, bottom=0),
                    content=ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.Icons.CHEVRON_LEFT,
                                icon_size=26,
                                icon_color=text_color2(),
                                width=28,
                                height=40,
                                padding=0,
                                tooltip="返回",
                                on_click=lambda e: on_back(),
                            ),
                            ft.Text(
                                "搜索",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=text_color(),
                            ),
                        ],
                        spacing=0,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(
                    padding=ft.padding.Padding(left=16, top=8, right=16, bottom=0),
                    content=ft.Row(
                        [
                            search_field,
                            ft.IconButton(
                                icon=ft.Icons.SEARCH,
                                icon_color="0x4A90D9",
                                tooltip="搜索",
                            ),
                        ],
                        spacing=4,
                    ),
                ),
                ft.Container(
                    padding=ft.padding.Padding(left=16, top=24, right=16, bottom=0),
                    content=ft.Column(
                        [
                            ft.Text(
                                "热门搜索",
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color=text_color2(),
                            ),
                            ft.Container(height=8),
                            hot_chips,
                        ],
                        spacing=0,
                    ),
                ),
            ],
            spacing=0,
            expand=True,
        ),
    )
