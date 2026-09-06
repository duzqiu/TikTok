"""
Profile view — 我的页面
"""
import flet as ft

STATUS_BAR_HEIGHT = 48
PAGE_HORIZONTAL_PADDING = 28

FUNCS = [
    ("收藏", ft.Icons.STAR, "0x64B5F6"),
    ("历史", ft.Icons.HISTORY, "0x81C784"),
    ("草稿箱", ft.Icons.DRAFTS, "0x81D4FA"),
    ("关注", ft.Icons.FAVORITE, "0x80CBC4"),
    ("消息", ft.Icons.CHAT, "0x90CAF9"),
    ("设置", ft.Icons.SETTINGS, "0xA5D6A7"),
]

# 设置列表: (名称, ICON, 颜色, 是否有开关)
SETTINGS_ITEMS = [
    ("账号安全", ft.Icons.SHIELD, "0x64B5F6", False),
    ("通知设置", ft.Icons.NOTIFICATIONS, "0x81C784", True),
    ("语言", ft.Icons.LANGUAGE, "0x81D4FA", False),
    ("地区设置", ft.Icons.PUBLIC, "0x80CBC4", False),
    ("清除缓存", ft.Icons.DELETE_SWEEP, "0x90CAF9", False),
    ("关于我们", ft.Icons.INFO, "0xA5D6A7", False),
]


def build_profile(
    page: ft.Page,
    gradient_colors,
    text_color,
    text_color2,
    text_color3,
    on_about=None,
    on_language=None,
    on_region=None,
    on_account_security=None,
    on_login=None,
    selected_language="中文简体",
    selected_region="中国",
    scroll_ref=None,
    on_scroll=None,
):
    def _func_item(icon, label, color):
        return ft.Container(
            width=52,
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
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, spacing=0)

    row2 = ft.Row([
        _func_item(FUNCS[3][1], FUNCS[3][0], FUNCS[3][2]),
        _func_item(FUNCS[4][1], FUNCS[4][0], FUNCS[4][2]),
        _func_item(FUNCS[5][1], FUNCS[5][0], FUNCS[5][2]),
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, spacing=0)

    card_bg = ft.Colors.with_opacity(
        0.7,
        "0x2A2A2A" if page.theme_mode == ft.ThemeMode.DARK else "white",
    )

    # 设置列表项
    setting_rows = []
    for name, icon, color, has_switch in SETTINGS_ITEMS:
        if has_switch:
            trailing = ft.Switch(value=False, active_color=color)
        elif name == "语言":
            trailing = ft.Row([
                ft.Text(selected_language, size=12, color=text_color3()),
                ft.Icon(ft.Icons.CHEVRON_RIGHT, size=20, color=text_color3()),
            ], spacing=4)
        elif name == "地区设置":
            trailing = ft.Row([
                ft.Text(selected_region, size=12, color=text_color3()),
                ft.Icon(ft.Icons.CHEVRON_RIGHT, size=20, color=text_color3()),
            ], spacing=4)
        else:
            trailing = ft.Icon(ft.Icons.CHEVRON_RIGHT, size=20, color=text_color3())
        setting_rows.append(
            ft.Container(
                padding=ft.padding.Padding(left=0, top=10, right=0, bottom=10),
                on_click=(
                    (lambda e: on_about()) if name == "关于我们" and on_about
                    else (lambda e: on_language()) if name == "语言" and on_language
                    else (lambda e: on_region()) if name == "地区设置" and on_region
                    else (lambda e: on_account_security()) if name == "账号安全" and on_account_security
                    else None
                ),
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
                padding=ft.padding.Padding(
                    left=PAGE_HORIZONTAL_PADDING, top=8,
                    right=PAGE_HORIZONTAL_PADDING, bottom=0,
                ),
                content=ft.Row([
                    ft.IconButton(
                        icon=ft.Icons.SUPPORT_AGENT,
                        icon_size=22,
                        icon_color="0x80CBC4",
                        tooltip="客服",
                        padding=0,
                        width=28,
                        height=28,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.QR_CODE_SCANNER,
                        icon_size=22,
                        icon_color="0x64B5F6",
                        tooltip="扫一扫",
                        padding=0,
                        width=28,
                        height=28,
                    ),
                ], alignment=ft.MainAxisAlignment.END, spacing=12),
            ),
            ft.Container(
                expand=True,
                content=ft.ListView(
                    ref=scroll_ref,
                    padding=ft.padding.Padding(left=0, top=0, right=0, bottom=0),
                    on_scroll=on_scroll,
                    build_controls_on_demand=False,
                    controls=[
                    ft.Container(
                        margin=ft.margin.Margin(
                            left=PAGE_HORIZONTAL_PADDING, top=16,
                            right=PAGE_HORIZONTAL_PADDING, bottom=0,
                        ),
                        padding=ft.padding.Padding(left=16, top=16, right=16, bottom=16),
                        border_radius=16,
                        bgcolor=card_bg,
                        content=ft.Column([
                            ft.Row([
                            # 头像盒子（30%）：头像居中
                            ft.Container(
                                expand=3,
                                alignment=ft.Alignment(0, 0),
                                on_click=(lambda e: on_login()) if on_login else None,
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
                                    content=ft.Icon(
                                        ft.Icons.ACCOUNT_CIRCLE,
                                        size=64,
                                        color="0x9E9E9E",
                                    ),
                                ),
                            ),
                            # 昵称ID盒子（70%）：内容居左
                            ft.Container(
                                expand=7,
                                alignment=ft.Alignment(-1, 0),
                                on_click=(lambda e: on_login()) if on_login else None,
                                content=ft.Column([
                                    ft.Text("登录/注册", size=18, weight=ft.FontWeight.W_500, color=text_color()),
                                    ft.Container(height=4),
                                    ft.Text("登录后查看个人主页", size=12, color=text_color3()),
                                ], horizontal_alignment=ft.CrossAxisAlignment.START, spacing=0),
                            ),
                            ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                            ft.Container(height=20),
                            # 数据展示：数字+名称，上下排列
                            ft.Row([
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
                        ], spacing=0),
                    ),
                    ft.Container(
                        margin=ft.margin.Margin(
                            left=PAGE_HORIZONTAL_PADDING, top=12,
                            right=PAGE_HORIZONTAL_PADDING, bottom=0,
                        ),
                        padding=ft.padding.Padding(left=16, top=16, right=16, bottom=16),
                        border_radius=16,
                        bgcolor=card_bg,
                        content=ft.Column([
                            ft.Text("常用功能", size=14, weight=ft.FontWeight.W_500, color=text_color2()),
                            ft.Container(height=16),
                            ft.Container(
                                margin=ft.margin.Margin(left=8, top=0, right=8, bottom=0),
                                content=row1,
                            ),
                            ft.Container(height=24),
                            ft.Container(
                                margin=ft.margin.Margin(left=8, top=0, right=8, bottom=0),
                                content=row2,
                            ),
                        ], spacing=0),
                    ),
                    ft.Container(
                        margin=ft.margin.Margin(
                            left=PAGE_HORIZONTAL_PADDING, top=12,
                            right=PAGE_HORIZONTAL_PADDING, bottom=0,
                        ),
                        padding=ft.padding.Padding(left=16, top=16, right=16, bottom=16),
                        border_radius=16,
                        bgcolor=card_bg,
                        content=ft.Column([
                            ft.Text("设置", size=14, weight=ft.FontWeight.W_500, color=text_color2()),
                            ft.Container(height=8),
                            ft.Container(
                                margin=ft.margin.Margin(left=8, top=0, right=8, bottom=0),
                                content=ft.Column(setting_rows, spacing=0),
                            ),
                        ], spacing=0),
                    ),
                    ft.Container(height=80),
                    ],
                    spacing=0,
                ),
            ),
        ], spacing=0, expand=True),
    )
