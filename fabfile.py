from fabric.api import local, run
from fabric.context_managers import cd

def gen_resume(templatename='resume.mako'):
    from mako.template import Template
    from mako.lookup import TemplateLookup

    mylookup = TemplateLookup(directories=['.'], module_directory='/tmp/mako_modules')
    mytemplate = mylookup.get_template(templatename)
    print(mytemplate.render())

def publish():
    local('resume publish')
