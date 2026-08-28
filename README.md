# Grok Bot 24/7 Keep-Alive Watchdog

自动维持 Grok Bot 会话活跃状态的看门狗守护程序，基于 GitHub Actions 云端 7x24 小时定时调度。

## 运行机制
* **调度频率**：每 10 分钟自动运行一次。
* **执行环境**：GitHub 官方云端 Runner。
* **安全保护**：凭据由 GitHub Encrypted Secrets 加密保护。

## 手动测试
进入本仓库的 **Actions** 标签页 -> 点击 **Grok Bot 24x7 Keep-Alive Watchdog** -> 点击 **Run workflow** 即可手动测试一次。
