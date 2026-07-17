import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, ALERT_EMAIL

def send_alert(subject, body, to_email=ALERT_EMAIL):
    if not SMTP_USER or not SMTP_PASSWORD:
        print("Credenciales de correo no configuradas. Alerta no enviada.")
        return False
    try:
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Error enviando correo: {e}")
        return False

def check_alerts_and_notify(kpis):
    """
    kpis: dict con 'revenue', 'orders', etc.
    """
    alerts = []
    if kpis['revenue'] < REVENUE_THRESHOLD:
        alerts.append(f"Ingresos bajos: {kpis['revenue']:.2f} € (umbral {REVENUE_THRESHOLD} €)")
    if kpis['orders'] < ORDERS_THRESHOLD:
        alerts.append(f"Pedidos bajos: {kpis['orders']} (umbral {ORDERS_THRESHOLD})")
    if alerts:
        subject = "⚠️ Alertas PulseBoard"
        body = "Se han detectado las siguientes anomalías:\n\n" + "\n".join(alerts)
        send_alert(subject, body)
