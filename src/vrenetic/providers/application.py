from backends import opencl

def info(version):
    print('Environment details:')
    print('Version:', version)
    try:
        has_opencl()
        print('OpenCL support: YES')
        print('--------OpenCL details--------')
        opencl_details()
    except:
        print('OpenCL support: NO')


def has_opencl():
    try:
        from backends import opencl
    except:
        raise ImportError('Cannot load OpenCL support')


def opencl_details():
    from backends import opencl
    opencl.details()

