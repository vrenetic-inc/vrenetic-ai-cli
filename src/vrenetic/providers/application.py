from backends import opencl

def info(version):
    print('----- Environment details ----')
    print('Version:', version)
    try:
        has_opencl()
        print('OpenCL support: YES')
    except:
        print('OpenCL support: NO')

    try:
        has_opencv()
        print('OpenCV support: YES')
    except:
        print('OpenCV support: NO')

    try:
        print()
        print('------- OpenCL details -------')
        opencl_details()
    except Exception as error:
        print('N/A')

    try:
        print()
        print('------- OpenCV details -------')
        opencv_details()
    except Exception as error:
        print('N/A')


def has_opencl():
    try:
        from backends import opencl
    except:
        raise ImportError('Cannot load OpenCL support')


def opencl_details():
    from backends import opencl
    opencl.details()


def has_opencv():
    raise Exception('Not implemented')


def opencv_details():
    raise Exception('Not implemented')

