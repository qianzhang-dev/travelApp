from manager import manager

from app import create_app

manager = Manager()

@manager.command
def run():
    """ Starts server on port 8000. """
    create_app()

if __name__ == '__main__':
    manager.main()