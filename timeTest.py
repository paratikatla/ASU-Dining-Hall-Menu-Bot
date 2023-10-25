from datetime import datetime, timedelta

now = datetime.now()
then = now + timedelta(days=1)
then = then.replace(hour=8, minute=0, second=0, microsecond=0)
print(then)