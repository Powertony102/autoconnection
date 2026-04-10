#!/usr/bin/env python3
"""
PhD 套瓷邮件发送工具 - v1.0
调用 QQ Mail Monitor 发送套磁信
"""

import json
import os
import sys
import re
from datetime import datetime
from typing import Dict, Any

# QQ Mail Monitor 路径
QQ_MAIL_MONITOR_PATH = "../qq-mail-monitor-1.0.0"


def extract_email_content(email_file: str) -> Dict[str, str]:
    """从生成的邮件文件中提取内容"""
    with open(email_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取主题
    subject_match = re.search(r'Subject:\s*(.+?)(?:\n|$)', content)
    subject = subject_match.group(1).strip() if subject_match else "PhD Application Inquiry"

    # 提取收件人（教授邮箱需要从主页或其他方式获取）
    # 这里返回邮件正文，邮箱地址需要用户手动提供
    return {
        "subject": subject,
        "body": content,
        "email_file": email_file
    }


def prepare_email_for_sending(
    professor_email: str,
    email_content: Dict[str, str],
    student_email: str,
    attachment_path: str = None
) -> str:
    """
    准备发送邮件的脚本命令
    返回需要在 qq_mail_send.py 中执行的代码片段
    """

    # 生成发送脚本
    script = f'''#!/usr/bin/env python3
"""
自动生成的套瓷邮件发送脚本
生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# 配置 - 从 QQ Mail Monitor 读取
EMAIL = "{student_email}"
AUTH_CODE = os.environ.get("QQ_AUTH_CODE", "your_auth_code")
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465

# 收件人
PROFESSOR_EMAIL = "{professor_email}"

# 邮件内容
SUBJECT = """{email_content['subject']}"""

BODY = """{email_content['body']}"""

def send_outreach_email():
    msg = MIMEMultipart("alternative")
    msg["From"] = EMAIL
    msg["To"] = PROFESSOR_EMAIL
    msg["Subject"] = SUBJECT

    # 添加邮件正文
    msg.attach(MIMEText(BODY, "plain", "utf-8"))

    # 添加附件（如果有）
    attachment = "{attachment_path if attachment_path else ''}"
    if attachment and os.path.exists(attachment):
        with open(attachment, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {{os.path.basename(attachment)}}",
        )
        msg.attach(part)
        print(f"📎 已附加文件: {{os.path.basename(attachment)}}")

    print("📤 正在发送套瓷邮件...")
    print(f"   发件人: {{EMAIL}}")
    print(f"   收件人: {{PROFESSOR_EMAIL}}")
    print(f"   主题: {{SUBJECT}}")

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(EMAIL, AUTH_CODE)
        server.send_message(msg)
        server.quit()

        print("\\n✅ 套瓷邮件发送成功！")
        print(f"   教授: {professor_email}")
        return True

    except Exception as e:
        print(f"\\n❌ 发送失败: {{e}}")
        return False

if __name__ == "__main__":
    send_outreach_email()
'''

    return script


def save_send_script(script_content: str, professor_name: str) -> str:
    """保存发送脚本"""
    os.makedirs("./outreach/scripts", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = professor_name.replace(" ", "_").replace(".", "")
    filename = f"./outreach/scripts/send_{safe_name}_{timestamp}.py"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(script_content)

    # 添加执行权限
    os.chmod(filename, 0o755)

    print(f"✅ 发送脚本已生成: {filename}")
    return filename


def list_pending_emails():
    """列出待发送的邮件"""
    emails_dir = "./outreach/emails"

    if not os.path.exists(emails_dir):
        print("❌ 没有已生成的套磁信")
        return []

    emails = []
    for f in os.listdir(emails_dir):
        if f.endswith('.md'):
            filepath = os.path.join(emails_dir, f)
            emails.append({
                "filename": f,
                "filepath": filepath,
                "created": os.path.getctime(filepath)
            })

    emails.sort(key=lambda x: x["created"], reverse=True)

    print("\n📧 已生成的套磁信列表:\n")
    for i, email in enumerate(emails, 1):
        created = datetime.fromtimestamp(email["created"]).strftime("%m-%d %H:%M")
        print(f"{i}. {email['filename']} ({created})")

    return emails


def generate_send_instructions(email_file: str) -> str:
    """生成发送指导"""
    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📤 邮件发送指导
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

邮件文件: {email_file}

发送步骤:
1. 找到教授的邮箱地址（通常在教授主页的 "Contact" 或 "Join Us" 页面）
2. 确保你的简历 PDF 已准备好
3. 运行以下命令发送:

   python3 {email_file.replace('.md', '.py')}

或者使用 QQ Mail Monitor:

   1. 复制邮件内容
   2. 打开 qq-mail-monitor-1.0.0/scripts/qq_mail_send.py
   3. 修改收件人、主题和正文
   4. 运行发送

注意事项:
- 发送前请仔细检查邮件内容
- 确保附件包含你的 CV
- 建议在邮件中提及 "I have attached my CV for your reference"
- 发送后可以在 outreach/sent/ 目录标记为已发送

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


def main():
    """主函数"""
    print("=" * 60)
    print("📤 PhD 套瓷邮件发送工具")
    print("=" * 60)
    print("\n此工具帮助生成邮件发送脚本。\n")

    # 列出待发送邮件
    emails = list_pending_emails()

    if not emails:
        print("\n请先生成套磁信: python3 generate_email.py")
        return

    print("\n使用方法:")
    print("1. 选择要发送的邮件编号")
    print("2. 提供教授邮箱地址")
    print("3. 确认发送")


if __name__ == "__main__":
    main()
