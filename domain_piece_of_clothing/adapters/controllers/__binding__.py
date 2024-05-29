from fastapi.applications import FastAPI

from .piece_of_clothing_controller import piece_of_clothing_controller


class Binding:
    def register_all(self, app: FastAPI) -> None:
        app.include_router(piece_of_clothing_controller)
