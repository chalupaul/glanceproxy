import sys, os, bottle

load_dir = os.path.join(os.sep, os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))), 'src')

sys.path = [load_dir] + sys.path
os.chdir(load_dir)
import glanceproxy
application = bottle.default_app()