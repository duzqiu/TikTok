"""Registration view."""
import asyncio

import flet as ft


def build_register(page, gradient_colors, text_color, text_color2, on_back):
    account_field = ft.TextField(
        hint_text="邮箱/手机号",
        border_radius=10,
        border_color=ft.Colors.with_opacity(0.35, "0x9E9E9E"),
        focused_border_color=ft.Colors.with_opacity(0.5, "0x9E9E9E"),
        content_padding=ft.padding.Padding(left=12, top=0, right=12, bottom=0),
        height=42,
    )
    code_field = ft.TextField(
        hint_text="验证码",
        border_radius=10,
        border_color=ft.Colors.with_opacity(0.35, "0x9E9E9E"),
        focused_border_color=ft.Colors.with_opacity(0.5, "0x9E9E9E"),
        content_padding=ft.padding.Padding(left=12, top=0, right=12, bottom=0),
        height=42,
        width=210,
    )
    status = ft.Text("", size=12, color=text_color2())
    countdown_label = ft.Text("获取验证码")
    send_code_button = ft.TextButton(
        content=countdown_label,
        width=100,
    )
    agreement = ft.Checkbox(value=False)
    register_button = ft.FilledButton(
        "注册",
        width=300,
        bgcolor="0xD6D6D6",
        color=ft.Colors.WHITE,
        disabled=True,
    )

    async def _countdown():
        for remaining in range(60, 0, -1):
            countdown_label.value = f"{remaining}s"
            page.update()
            await asyncio.sleep(1)
        countdown_label.value = "获取验证码"
        send_code_button.disabled = False
        page.update()

    def _send_code(e):
        if not account_field.value or not account_field.value.strip():
            status.value = "请先输入邮箱或手机号"
            page.update()
            return
        send_code_button.disabled = True
        countdown_label.value = "60s"
        status.value = "验证码已发送，请查收"
        page.update()
        page.run_task(_countdown)

    send_code_button.on_click = _send_code

    def _show_register_agreement(e):
        page.show_dialog(ft.SnackBar(content=ft.Text("注册协议页面即将开放")))

    def _update_register_state(e=None):
        ready = bool(
            account_field.value
            and account_field.value.strip()
            and code_field.value
            and code_field.value.strip()
            and agreement.value
        )
        register_button.disabled = not ready
        register_button.bgcolor = "0x64B5F6" if ready else "0xD6D6D6"
        page.update()

    account_field.on_change = _update_register_state
    code_field.on_change = _update_register_state
    agreement.on_change = _update_register_state

    def _submit_register(e):
        if not account_field.value or not account_field.value.strip():
            status.value = "请先输入邮箱或手机号"
        elif not code_field.value or not code_field.value.strip():
            status.value = "请输入验证码"
        else:
            status.value = "注册成功，请返回登录"
        page.update()

    register_button.on_click = _submit_register

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
                            ft.Text("注册", size=18, color=text_color()),
                        ],
                        spacing=0,
                    ),
                ),
                ft.Container(height=24),
                ft.Image(src="icon.png", width=72, height=72, fit="contain"),
                ft.Container(height=16),
                ft.Text("创建你的账号", size=18, color=text_color()),
                ft.Container(height=56),
                ft.Container(width=300, content=account_field),
                ft.Container(height=20),
                ft.Row(
                    [
                        code_field,
                        send_code_button,
                    ],
                    width=300,
                    spacing=8,
                ),
                ft.Container(height=0),
                ft.Container(
                    width=300,
                    content=ft.Row(
                        [
                            agreement,
                            ft.Text("我已阅读并同意", size=12, color=text_color2()),
                            ft.TextButton(
                                content=ft.Text("注册协议", size=12, color="0x2196F3"),
                                on_click=_show_register_agreement,
                                style=ft.ButtonStyle(padding=0),
                            ),
                        ],
                        spacing=0,
                    ),
                ),
                ft.Container(height=28),
                register_button,
                status,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            expand=True,
        ),
    )
