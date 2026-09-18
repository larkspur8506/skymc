#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import requests
from datetime import datetime, timezone, timedelta

SERVER_NAME = "zdsa"
SERVER_ID = "TuUzR_dWxO2P"
SERVER_URL = "https://skymc.org/en/server/TuUzR_dWxO2P"
SERVER_ADDRESS = "zdsa.skymc.io"

TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "")
TG_CHAT_ID = os.getenv("TG_CHAT_ID", "")


def send_telegram(text: str):
    if not TG_BOT_TOKEN or not TG_CHAT_ID:
        print("⚠️  未配置 TG_BOT_TOKEN 或 TG_CHAT_ID")
        return False
    try:
        resp = requests.post(
            f"https://api.telegram.org/bot{TG_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": TG_CHAT_ID,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": True,
            },
            timeout=15,
        )
        return resp.status_code == 200
    except Exception as e:
        print(f"❌ 发送异常: {e}")
        return False


def main():
    bj = timezone(timedelta(hours=8))
    now = datetime.now(bj).strftime("%Y-%m-%d %H:%M:%S")
    msg = f"""🔔 <b>SkyMC 免费服务器续期提醒</b>

服务器：<code>{SERVER_NAME}</code>
ID：<code>{SERVER_ID}</code>
地址：<code>{SERVER_ADDRESS}</code>

面板：{SERVER_URL}

请尽快登录并点击蓝色 <b>Renew</b> 按钮！

时间：{now}（北京时间）"""
    print(msg.replace("<b>", "").replace("</b>", "").replace("<code>", "").replace("</code>", ""))
    send_telegram(msg)
    print("提醒完成")


if __name__ == "__main__":
    main()
