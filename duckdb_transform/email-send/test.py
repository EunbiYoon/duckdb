import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

recipients = ["bianca.yoon@cheilpengtai.com", "juu.jeon@cheilpengtai.com"]

msg = MIMEText("server 본문 내용입니다")
msg["Subject"] = "테스트 메일"
msg["From"] = formataddr(("재무지표시스템", "webmaster@121.252.183.58"))
msg["To"] = ", ".join(recipients)  # 보기용 문자열
# ✅ recipients는 진짜 이메일 리스트로 사용해야 함

with smtplib.SMTP("mailin.samsung.com", 25) as server:
    server.sendmail(msg["From"], recipients, msg.as_string())  # ✅ 고쳤음!