from backends import opencl

def info(version):
    print('Environment details:')
    print('Version:', version)
    try:
        has_opencl()
        print('OpenCL support: YES')
    except:
        print('OpenCL support: NO')

    # print('--------OpenCL autotest--------')
    # opencl_autotest()


def has_opencl():
    try:
        from backends import opencl
    except:
        raise ImportError('Cannot load OpenCL support')


def opencl_autotest():
    from backends import opencl
    opencl.performance_test()

