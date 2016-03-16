from fabric.api import local, run
from fabric.context_managers import cd

def gen_resume(templatename='resume.mako', output='resume.json'):
    from mako.template import Template
    from mako.lookup import TemplateLookup

    mylookup = TemplateLookup(directories=['.'], module_directory='mako_modules')
    mytemplate = mylookup.get_template(templatename)
    with open(output, "w") as f:
        f.write(mytemplate.render())
    print "Done!"
    local('resume test')

def publish(theme='slick'):
    """Good themes
    elegant
    slick
    """
    local('resume publish --theme {0}'.format(theme))
