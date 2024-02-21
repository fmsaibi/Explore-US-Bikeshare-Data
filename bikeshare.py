"""
Bikeshare
"""
from app.controller.backshare_controller import BackshareController

if __name__ == "__main__":
    controller = BackshareController()
    controller.run_app()
