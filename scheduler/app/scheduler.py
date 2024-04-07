import logging
import schedule
import httpx

logging.basicConfig(level=logging.INFO)


def notify_about_ending_liabilities():
    httpx.get("http://notifications-service:8009/notify-ending-mots-or-insurances/7", timeout=60)


schedule.every().day.at("08:00", "Europe/Amsterdam").do(notify_about_ending_liabilities)

if __name__ == "__main__":
    logging.info('Scheduler started. Waiting for pending actions...')
    while True:
        schedule.run_pending()
