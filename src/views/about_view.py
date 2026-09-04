"""About view — 关于我们页面"""
import flet as ft

STATUS_BAR_HEIGHT = 48
PAGE_HORIZONTAL_PADDING = 28


def build_about(page, gradient_colors, text_color, text_color2, text_color3, on_back=None):
    card_bg = ft.Colors.with_opacity(
        0.7,
        "0x2A2A2A" if page.theme_mode == ft.ThemeMode.DARK else "white",
    )

    def _contact_item(icon, color, label, value):
        return ft.Container(
            padding=ft.padding.Padding(left=0, top=12, right=0, bottom=12),
            content=ft.Row([
                ft.Container(
                    width=36, height=36, border_radius=18,
                    bgcolor=ft.Colors.with_opacity(0.16, color),
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(icon, size=19, color=color),
                ),
                ft.Container(width=12),
                ft.Text(label, size=14, color=text_color(), expand=True),
                ft.Text(value, size=12, color=text_color3()),
            ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
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
                    ft.Text("关于我们", size=20, weight=ft.FontWeight.W_500, color=text_color()),
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
                        padding=ft.padding.Padding(left=20, top=24, right=20, bottom=24),
                        border_radius=16,
                        bgcolor=card_bg,
                        alignment=ft.Alignment.CENTER,
                        content=ft.Column([
                            ft.Container(
                                width=72, height=72, border_radius=16,
                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                content=ft.Image(src="icon.png", fit="cover"),
                            ),
                            ft.Container(height=12),
                            ft.Text("TikTok", size=20, weight=ft.FontWeight.BOLD, color=text_color()),
                            ft.Container(height=4),
                            ft.Text("版本 0.1.0", size=12, color=text_color3()),
                            ft.Container(height=16),
                            ft.Text(
                                "记录有趣生活，发现更多精彩内容。",
                                size=13,
                                color=text_color2(),
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                    ),
                    ft.Container(
                        margin=ft.margin.Margin(
                            left=PAGE_HORIZONTAL_PADDING, top=16,
                            right=PAGE_HORIZONTAL_PADDING, bottom=0,
                        ),
                        padding=ft.padding.Padding(left=16, top=8, right=16, bottom=8),
                        border_radius=16,
                        bgcolor=card_bg,
                        content=ft.Column([
                            _contact_item(ft.Icons.EMAIL, "0x64B5F6", "邮箱", "support@tiktok.com"),
                            _contact_item(ft.Icons.PHONE, "0x81C784", "客服电话", "400-888-8888"),
                            _contact_item(ft.Icons.LANGUAGE, "0x81D4FA", "官方网站", "www.tiktok.com"),
                            _contact_item(ft.Icons.CHAT_BUBBLE_OUTLINE, "0x80CBC4", "在线反馈", "工作日 9:00-18:00"),
                        ], spacing=0),
                    ),
                ],
            ),
        ], spacing=0, expand=True),
    )
