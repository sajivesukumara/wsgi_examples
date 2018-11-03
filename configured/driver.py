if __name__ == '__main__':
    from paste import httpserver
    from paste.deploy import loadapp
    httpserver.serve(loadapp('config:configured.ini', relative_to='.'),
                     host='127.0.0.1', port='8080')

