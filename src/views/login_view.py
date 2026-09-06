"""Login view."""
import flet as ft


def build_login(page, gradient_colors, text_color, text_color2, on_back, on_register):
    account_field = ft.TextField(
        hint_text="手机号/邮箱",
        border_radius=10,
        border_color=ft.Colors.with_opacity(0.35, "0x9E9E9E"),
        focused_border_color=ft.Colors.with_opacity(0.5, "0x9E9E9E"),
        content_padding=ft.padding.Padding(left=12, top=0, right=12, bottom=0),
        height=42,
    )
    password_field = ft.TextField(
        hint_text="密码",
        password=True,
        can_reveal_password=True,
        border_radius=10,
        border_color=ft.Colors.with_opacity(0.35, "0x9E9E9E"),
        focused_border_color=ft.Colors.with_opacity(0.5, "0x9E9E9E"),
        content_padding=ft.padding.Padding(left=12, top=0, right=12, bottom=0),
        height=42,
    )
    agreement = ft.Checkbox(value=False)
    login_button = ft.FilledButton(
        "登录",
        width=300,
        bgcolor="0xD6D6D6",
        color=ft.Colors.WHITE,
        disabled=True,
    )

    def _update_login_state(e=None):
        ready = bool(
            account_field.value
            and account_field.value.strip()
            and password_field.value
            and password_field.value.strip()
            and agreement.value
        )
        login_button.disabled = not ready
        login_button.bgcolor = "0x64B5F6" if ready else "0xD6D6D6"
        page.update()

    account_field.on_change = _update_login_state
    password_field.on_change = _update_login_state
    agreement.on_change = _update_login_state

    def _show_login_agreement(e):
        page.show_dialog(ft.SnackBar(content=ft.Text("登录协议页面即将开放")))

    return ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=gradient_colors(),
        ),
        content=ft.Column(
            [
                ft.Container(height=48),
                ft.Container(
                    padding=ft.padding.Padding(left=20, top=8, right=20, bottom=8),
                    content=ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.Icons.CHEVRON_LEFT,
                                icon_size=26,
                                icon_color=text_color2(),
                                width=28,
                                height=40,
                                padding=0,
                                on_click=lambda e: on_back(),
                            ),
                            ft.Text("登录/注册", size=18, color=text_color()),
                        ],
                        spacing=0,
                    ),
                ),
                ft.Container(height=24),
                ft.Image(
                    src="icon.png",
                    width=72,
                    height=72,
                    fit="contain",
                ),
                ft.Container(height=16),
                ft.Text("登录后享受更多功能", size=18, color=text_color()),
                ft.Container(height=56),
                ft.Container(width=300, content=account_field),
                ft.Container(height=20),
                ft.Container(width=300, content=password_field),
                ft.Container(
                    width=300,
                    content=ft.Row(
                        [
                            agreement,
                            ft.Text("我已阅读并同意", size=12, color=text_color2()),
                            ft.TextButton(
                                content=ft.Text("登录协议", size=12, color="0x2196F3"),
                                on_click=_show_login_agreement,
                                style=ft.ButtonStyle(
                                    padding=0,
                                ),
                            ),
                        ],
                        spacing=0,
                    ),
                ),
                ft.Container(height=28),
                login_button,
                ft.Container(height=20),
                ft.TextButton(
                    "注册",
                    on_click=lambda e: on_register(),
                    style=ft.ButtonStyle(color=text_color2()),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            expand=True,
        ),
    )
