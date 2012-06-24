import os, yaml, requests
from bottle import route, run, debug

conf_file = os.path.join(os.sep, os.path.dirname(
        os.path.dirname(os.path.realpath(__file__))),
                         'conf', 'glanceproxy.yaml')
confs = yaml.load(open(conf_file))

@route('/test')
def test():
    return __name__

if __name__ == '__main__':
    debug(True)
    run(reloader=True)

