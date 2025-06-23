import json
import os
import threading

from flask import Response

from configs import config


def init_app(app):
    @app.after_request
    def after_request(response):
        """Add Version headers to the response."""
        response.headers.add("X-Version", config.CURRENT_VERSION)
        return response

    @app.route("/health")
    def health():
        return Response(
            json.dumps({"pid": os.getpid(), "status": "ok", "version": config.CURRENT_VERSION}),
            status=200,
            content_type="application/json",
        )

    @app.route("/threads")
    def threads():
        num_threads = threading.active_count()
        threads = threading.enumerate()

        thread_list = []
        for thread in threads:
            thread_name = thread.name
            thread_id = thread.ident
            is_alive = thread.is_alive()

            thread_list.append(
                {
                    "name": thread_name,
                    "id": thread_id,
                    "is_alive": is_alive,
                }
            )

        return {
            "pid": os.getpid(),
            "thread_num": num_threads,
            "threads": thread_list,
        }