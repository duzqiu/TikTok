"""
Explore view — 发现页面
"""
import flet as ft

STATUS_BAR_HEIGHT = 48


def build_explore(
    page: ft.Page,
    gradient_colors,
    text_color,
    text_color2,
    on_search_focus=None,
    on_back=None,
):
    hot_words = [
        "iPhone 17", "AI大模型", "新能源汽车", "世界杯",
        "秋季穿搭", "电影推荐", "健康饮食", "旅行攻略",
        "健身计划", "数码测评", "直播带货", "短视频创作",
    ]
    hot_rankings = [
        ("iPhone 17", "128.6万"),
        ("AI大模型", "96.4万"),
        ("新能源汽车", "82.1万"),
        ("世界杯", "76.8万"),
        ("秋季穿搭", "64.3万"),
        ("电影推荐", "58.7万"),
        ("健康饮食", "52.4万"),
        ("旅行攻略", "47.9万"),
        ("健身计划", "43.6万"),
        ("数码测评", "39.8万"),
        ("数码测评", "39.8万"),
        ("数码测评", "39.8万"),
        ("数码测评", "39.8万"),
        ("数码测评", "39.8万"),
        ("数码测评", "39.8万"),
        ("数码测评", "39.8万"),
        ("数码测评数码测评数码测评数码测评数码测评数码测评数码测评数码测评数码测评数码测评", "39.8万"),
        ("数码测评", "39.8万"),
        ("数码测评", "39.8万"),
    ]

    # 搜索框盒子（无背景色，紧凑样式）
    search_box = ft.Container(
        expand=True,
        alignment=ft.Alignment(0, -1),
        padding=ft.padding.Padding(left=24, top=0, right=24, bottom=0),
        content=ft.TextField(
            hint_text="搜索内容、用户或话题",
            border_radius=12,
            border_color="0xE0E0E0",
            focused_border_color="0xE0E0E0",
            text_size=13,
            expand=True,
            border_width=0.5,
            focused_border_width=0.5,
            content_padding=ft.padding.Padding(left=12, top=2, right=12, bottom=2),
            on_focus=lambda e: on_search_focus(True) if on_search_focus else None,
            on_blur=lambda e: on_search_focus(False) if on_search_focus else None,
        ),
    )

    # 热搜词盒子
    hot_chips_row = ft.Row(spacing=8, wrap=True)
    for word in hot_words:
        hot_chips_row.controls.append(
            ft.Container(
                padding=ft.padding.Padding(left=12, top=6, right=12, bottom=6),
                border_radius=16,
                bgcolor=ft.Colors.with_opacity(0.1, "0x4A90D9"),
                content=ft.Text(word, size=12, color="0x4A90D9"),
            )
        )
    ranking_rows = []
    for index, (word, value) in enumerate(hot_rankings, start=1):
        ranking_rows.append(
            ft.Row(
                [
                    ft.Container(
                        width=24,
                        height=24,
                        border_radius=6,
                        bgcolor=(
                            "0xFF7043" if index == 1
                            else "0xFFB74D" if index == 2
                            else "0xFFD54F" if index == 3
                            else ft.Colors.with_opacity(0.12, "0x4A90D9")
                        ),
                        alignment=ft.Alignment.CENTER,
                        content=ft.Text(
                            str(index),
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE if index <= 3 else text_color2(),
                        ),
                    ),
                    ft.Text(
                        word,
                        size=13,
                        color=text_color2(),
                        max_lines=1,
                        overflow=ft.TextOverflow.ELLIPSIS,
                        expand=True,
                    ),
                    ft.Row(
                        [
                            ft.Icon(
                                ft.Icons.LOCAL_FIRE_DEPARTMENT,
                                size=16,
                                color="0xFF7043",
                            ),
                            ft.Text(value, size=12, color=text_color2()),
                        ],
                        width=76,
                        spacing=4,
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    ranking_box = ft.Container(
        expand=True,
        margin=ft.margin.Margin(left=24, top=20, right=24, bottom=20),
        padding=ft.padding.Padding(left=0, top=0, right=0, bottom=0),
        content=ft.Column(
            [
                ft.Text(
                    "热搜榜",
                    size=14,
                    weight=ft.FontWeight.W_500,
                    color=text_color2(),
                ),
                ft.Container(
                    padding=ft.padding.Padding(left=8, top=0, right=0, bottom=0),
                    content=ft.Column(ranking_rows, spacing=8),
                ),
            ],
            spacing=8,
        ),
    )
    hot_box = ft.Container(
        expand=True,
        margin=ft.margin.Margin(left=24, top=10, right=24, bottom=0),
        content=ft.Column(
            [
                ft.Text("热搜", size=14, weight=ft.FontWeight.W_500, color=text_color2()),
                ft.Container(height=6),
                hot_chips_row,
            ],
            spacing=0,
        ),
    )

    page_header = ft.Container(height=12)
    if on_back is not None:
        page_header = ft.Container(
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
        )
    page_content = [
        ft.Container(height=0 if on_back is not None else 12),
        search_box,
        hot_box,
        ranking_box,
        ft.Container(height=80),
    ]

    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Stack(
            [
                ft.Container(
                    top=0,
                    left=0,
                    right=0,
                    height=STATUS_BAR_HEIGHT,
                    bgcolor=gradient_colors()[0],
                ),
                ft.Container(
                    top=STATUS_BAR_HEIGHT,
                    left=0,
                    right=0,
                    bottom=0,
                    content=ft.Column(
                        [
                            page_header,
                            ft.Column(
                                page_content,
                                spacing=0,
                                scroll=ft.ScrollMode.AUTO,
                                expand=True,
                            ),
                        ],
                        spacing=0,
                        expand=True,
                    ),
                ),
            ],
            expand=True,
        ),
    )
