"""Account security view — 账号与安全页面"""
import flet as ft

STATUS_BAR_HEIGHT = 48
PAGE_HORIZONTAL_PADDING = 28


def build_account_security(page, gradient_colors, text_color, text_color2, text_color3,
                           on_back=None):
    card_bg = ft.Colors.with_opacity(
        0.7,
        "0x2A2A2A" if page.theme_mode == ft.ThemeMode.DARK else "white",
    )

    def _item(icon, color, label, trailing):
        return ft.Container(
            padding=ft.padding.Padding(left=0, top=14, right=0, bottom=14),
            content=ft.Row([
                ft.Container(
                    width=36, height=36, border_radius=18,
                    bgcolor=ft.Colors.with_opacity(0.16, color),
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(icon, size=19, color=color),
                ),
                ft.Container(width=12),
                ft.Text(label, size=15, color=text_color(), expand=True),
                trailing,
            ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
        )

    arrow = lambda: ft.Icon(ft.Icons.CHEVRON_RIGHT, size=20, color=text_color3())

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
                    ft.Text("账号与安全", size=16, weight=ft.FontWeight.W_500, color=text_color()),
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
                        padding=ft.padding.Padding(left=16, top=4, right=16, bottom=4),
                        border_radius=16,
                        bgcolor=card_bg,
                        content=ft.Column([
                            _item(
                                ft.Icons.EMAIL, "0x64B5F6", "邮箱",
                                ft.Text("user@example.com", size=12, color=text_color3()),
                            ),
                            _item(ft.Icons.LOCK_OUTLINE, "0x81C784", "修改密码", arrow()),
                            _item(ft.Icons.BLOCK, "0x81D4FA", "黑名单", arrow()),
                        ], spacing=0),
                    ),
                ],
            ),
        ], spacing=0, expand=True),
    )
