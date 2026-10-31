name: Visa Appointment Checker

on:
  schedule:
    - cron: '*/5 * * * *'  # يعمل تلقائياً كل 5 دقائق
  workflow_dispatch:      # لتمكين التشغيل اليدوي متى أردت

jobs:
  run-bot:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install selenium requests

      - name: Run bot script
        run: python bot.py
