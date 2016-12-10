from flask_script import Manager
from ssbase import create_app

the_app=create_app()

manager = Manager(the_app)

if __name__ == '__main__':
    manager.run()
    
    
@manager.command
def run_app():
    
    the_app.run(debug=False)