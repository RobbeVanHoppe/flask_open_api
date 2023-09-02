from connexion import App
import asyncio

app = App(__name__)
app.add_api("backend.yaml")


async def run_server():
    from hypercorn.config import Config
    config = Config()
    config.bind = ["127.0.0.1:8000"]

    from hypercorn.asyncio import serve
    await serve(app, config)

if __name__ == '__main__':
    asyncio.run(run_server())
