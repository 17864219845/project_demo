from datetime import timedelta
from celery import Celery, Task  # type: ignore
from celery.schedules import crontab  # type: ignore
from configs import config


def init_app(app) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(
        app.name,
        task_cls=FlaskTask,
        broker=config.CELERY_BROKER_URL,
        task_ignore_result=True,
    )

    celery_app.conf.update(
        result_backend=config.CELERY_RESULT_BACKEND,
        broker_connection_retry_on_startup=True,
        worker_log_format=config.CELERY_LOG_FORMAT,
        worker_task_log_format=config.CELERY_LOG_FORMAT,
        worker_hijack_root_logger=False,
        timezone="UTC",
    )

    celery_app.set_default()
    app.extensions["celery"] = celery_app

    # Celery 能找到任务函数
    imports = [
        "schedule.output_time",
    ]
    beat_schedule = {
        "output_time": {
            "task": "schedule.output_time.output_time",
            "schedule": timedelta(seconds=5),
        },
    }
    celery_app.conf.update(beat_schedule=beat_schedule, imports=imports)

    return celery_app
