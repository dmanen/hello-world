def options(opt):
        opt.load('compiler_c')

def configure(conf):
        conf.load('compiler_c')

def build(bld):
        bld.program(source='hello.c', target='hello')
