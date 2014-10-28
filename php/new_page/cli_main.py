import cli.app


@cli.app.CommandLineApp
def cg(app):
    pass

cg.add_param('-p', '--project', help='The root path of project.', default=False, action='')

if "__main__" == __name__:
    cg.run()
