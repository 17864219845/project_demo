import app


@app.celery.task(queue="dataset")
def output_time():
    from datetime import datetime
    now = datetime.now()
    print("当前时间是：", now.strftime("%Y-%m-%d %H:%M:%S"))
