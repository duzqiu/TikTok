"""
Profile view — 我的页面
"""
import flet as ft

STATUS_BAR_HEIGHT = 48

FUNCS = [
    ("收藏", ft.Icons.STAR, "0xFF9800"),
    ("历史", ft.Icons.HISTORY, "0x4CAF50"),
    ("草稿箱", ft.Icons.DRAFTS, "0x2196F3"),
    ("关注", ft.Icons.FAVORITE, "0xE91E63"),
    ("消息", ft.Icons.CHAT, "0x9C27B0"),
    ("设置", ft.Icons.SETTINGS, "0x4A90D9"),
]

# 设置列表: (名称, ICON, 颜色, 是否有开关)
SETTINGS_ITEMS = [
    ("账号安全", ft.Icons.SHIELD, "0x4A90D9", False),
    ("通知设置", ft.Icons.NOTIFICATIONS, "0xFF9800", True),
    ("语言", ft.Icons.LANGUAGE, "0x9C27B0", False),
    ("地区设置", ft.Icons.PUBLIC, "0x2196F3", False),
    ("清除缓存", ft.Icons.DELETE_SWEEP, "0xE91E63", False),
    ("关于我们", ft.Icons.INFO, "0x4CAF50", False),
]


def build_profile(
    page: ft.Page,
    gradient_colors,
    text_color,
    text_color2,
    text_color3,
):
    def _func_item(icon, label, color):
        return ft.Container(
            expand=True,
            alignment=ft.Alignment.CENTER,
            content=ft.Column([
                ft.Container(
                    width=52, height=52, border_radius=26,
                    bgcolor=ft.Colors.with_opacity(0.15, color),
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(icon, size=26, color=color),
                ),
                ft.Container(height=6),
                ft.Text(label, size=12, color=text_color2()),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
        )

    row1 = ft.Row([
        _func_item(FUNCS[0][1], FUNCS[0][0], FUNCS[0][2]),
        _func_item(FUNCS[1][1], FUNCS[1][0], FUNCS[1][2]),
        _func_item(FUNCS[2][1], FUNCS[2][0], FUNCS[2][2]),
    ], spacing=8, expand=True)

    row2 = ft.Row([
        _func_item(FUNCS[3][1], FUNCS[3][0], FUNCS[3][2]),
        _func_item(FUNCS[4][1], FUNCS[4][0], FUNCS[4][2]),
        _func_item(FUNCS[5][1], FUNCS[5][0], FUNCS[5][2]),
    ], spacing=8, expand=True)

    # 设置列表项
    setting_rows = []
    for name, icon, color, has_switch in SETTINGS_ITEMS:
        if has_switch:
            trailing = ft.Switch(value=False, active_color=color)
        else:
            trailing = ft.Icon(ft.Icons.CHEVRON_RIGHT, size=20, color=text_color3())
        setting_rows.append(
            ft.Container(
                padding=ft.padding.Padding(left=4, top=10, right=4, bottom=10),
                content=ft.Row([
                    ft.Container(
                        width=32, height=32, border_radius=16,
                        bgcolor=ft.Colors.with_opacity(0.12, color),
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(icon, size=18, color=color),
                    ),
                    ft.Container(width=12),
                    ft.Text(name, size=14, color=text_color(), expand=True),
                    trailing,
                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
            )
        )

    # 固定顶部状态栏 + 可滚动内容
    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1), end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Column([
            ft.Container(height=STATUS_BAR_HEIGHT),
            ft.Container(
                padding=ft.padding.Padding(left=16, top=8, right=16, bottom=0),
                content=ft.Row([
                    ft.Text("我的", size=20, weight=ft.FontWeight.W_500, color=text_color()),
                ]),
            ),
            ft.Container(
                expand=True,
                content=ft.ListView(
                    padding=ft.padding.Padding(left=0, top=0, right=0, bottom=0),
                    controls=[
                    ft.Container(
                        padding=ft.padding.Padding(left=16, top=16, right=16, bottom=0),
                        content=ft.Row([
                            # 头像盒子（30%）：头像居中
                            ft.Container(
                                expand=3,
                                alignment=ft.Alignment(0, 0),
                                content=ft.Container(
                                    width=64, height=64, border_radius=32,
                                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                    border=ft.border.Border(
                                        top=ft.BorderSide(1, "0xCCCCCC"),
                                        bottom=ft.BorderSide(1, "0xCCCCCC"),
                                        left=ft.BorderSide(1, "0xCCCCCC"),
                                        right=ft.BorderSide(1, "0xCCCCCC"),
                                    ),
                                    alignment=ft.Alignment.CENTER,
                                    content=ft.Image(
                                        src="https://api.dicebear.com/9.x/adventurer/png?seed=TikTok&size=128",
                                        fit="cover",
                                        width=64, height=64,
                                    ),
                                ),
                            ),
                            # 昵称ID盒子（70%）：内容居左
                            ft.Container(
                                expand=7,
                                alignment=ft.Alignment(-1, 0),
                                content=ft.Column([
                                    ft.Text("TikTok用户", size=18, weight=ft.FontWeight.W_500, color=text_color()),
                                    ft.Container(height=4),
                                    ft.Text("ID: 88888888", size=12, color=text_color3()),
                                ], horizontal_alignment=ft.CrossAxisAlignment.START, spacing=0),
                            ),
                        ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                    ),
                    # 数据展示：数字+名称，上下排列
                    ft.Container(
                        margin=ft.margin.Margin(left=16, top=12, right=16, bottom=0),
                        content=ft.Row([
                            ft.Container(
                                expand=True,
                                content=ft.Column([
                                    ft.Text("12", size=16, weight=ft.FontWeight.BOLD, color=text_color()),
                                    ft.Container(height=4),
                                    ft.Text("作品", size=11, color=text_color3()),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                            ),
                            ft.Container(
                                expand=True,
                                content=ft.Column([
                                    ft.Text("1.2万", size=16, weight=ft.FontWeight.BOLD, color=text_color()),
                                    ft.Container(height=4),
                                    ft.Text("粉丝", size=11, color=text_color3()),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                            ),
                            ft.Container(
                                expand=True,
                                content=ft.Column([
                                    ft.Text("368", size=16, weight=ft.FontWeight.BOLD, color=text_color()),
                                    ft.Container(height=4),
                                    ft.Text("关注", size=11, color=text_color3()),
                                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                            ),
                        ], spacing=8),
                    ),
                    ft.Container(
                        margin=ft.margin.Margin(left=4, top=12, right=4, bottom=0),
                        padding=ft.padding.Padding(left=8, top=12, right=8, bottom=0),
                        content=ft.Column([
                            ft.Text("常用功能", size=14, weight=ft.FontWeight.W_500, color=text_color2()),
                            ft.Container(height=16),
                            row1,
                            ft.Container(height=24),
                            row2,
                        ], spacing=0),
                    ),
                    ft.Container(
                        margin=ft.margin.Margin(left=4, top=12, right=4, bottom=0),
                        padding=ft.padding.Padding(left=8, top=16, right=8, bottom=0),
                        content=ft.Column([
                            ft.Text("设置", size=14, weight=ft.FontWeight.W_500, color=text_color2()),
                            ft.Container(height=8),
                            ft.Column(setting_rows, spacing=0),
                        ], spacing=0),
                    ),
                    ft.Container(height=80),
                    ],
                    spacing=0,
                ),
            ),
        ], spacing=0, expand=True),
    )
