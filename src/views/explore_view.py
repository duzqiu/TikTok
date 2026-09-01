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
):
    hot_words = [
        "iPhone 17", "AI大模型", "新能源汽车", "世界杯",
        "秋季穿搭", "电影推荐", "健康饮食", "旅行攻略",
        "健身计划", "数码测评", "直播带货", "短视频创作",
    ]

    # 搜索框盒子（无背景色，紧凑样式）
    search_box = ft.Container(
        alignment=ft.Alignment(0, -1),
        padding=ft.padding.Padding(left=16, top=0, right=16, bottom=0),
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
    hot_box = ft.Container(
        margin=ft.margin.Margin(left=16, top=10, right=16, bottom=0),
        content=ft.Column([
            ft.Text("热搜", size=14, weight=ft.FontWeight.W_500, color=text_color2()),
            ft.Container(height=6),
            hot_chips_row,
        ], spacing=0),
    )

    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Column([
            ft.Container(height=STATUS_BAR_HEIGHT),
            ft.Container(height=12),
            search_box,
            hot_box,
        ], spacing=0, expand=True),
    )
