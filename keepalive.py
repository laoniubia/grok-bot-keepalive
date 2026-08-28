import os
import sys
import time
import requests

TOKEN = os.getenv("GROK_TOKEN", "").strip()
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

def run_heartbeat():
    now_str = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now_str}] 🚀 启动 Grok Bot 自动保活看门狗...")
    
    session = requests.Session()
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
        "Referer": "https://grok.com/",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
        cookies = {
            "sso": TOKEN,
            "sso-rw": TOKEN,
            "auth_token": TOKEN,
            "session": TOKEN,
        }
        session.cookies.update(cookies)
    
    targets = [
        "https://grok.com",
        "https://grok.com/api/user",
        "https://api.x.ai/v1/models",
    ]
    
    success = False
    for url in targets:
        try:
            resp = session.get(url, headers=headers, timeout=15)
            print(f"-> [PING] {url} | 状态码: {resp.status_code}")
            if resp.status_code in [200, 302, 304]:
                success = True
        except Exception as e:
            print(f"-> [WARN] 请求 {url} 异常: {e}")
            
    if success:
        print(f"[{now_str}] ✅ 保活心跳发送成功！会话保持活跃。")
    else:
        print(f"[{now_str}] ⚠️ 心跳完成，保持待命状态。")

if __name__ == "__main__":
    run_heartbeat()
