

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
        has_pytorch()
        print('PyTorch support: YES')
    except:
        print('PyTorch support: NO')

    try:
        print()
        print('------- OpenCL details -------')
        opencl_details()
    except Exception as error:
        print(error)

    try:
        print()
        print('------- OpenCV details -------')
        opencv_details()
    except Exception as error:
        print(error)

    try:
        print()
        print('------- PyTorch details -------')
        pytorch_details()
    except Exception as error:
        print(error)


def has_opencl():
    try:
        from backends import opencl
    except:
        raise ImportError('Cannot load OpenCL support')


def opencl_details():
    from backends import opencl
    opencl.details()


def has_opencv():
    try:
        from backends import opencv
    except:
        raise ImportError('Cannot load OpenCV support')


def opencv_details():
    from backends import opencv
    opencv.details()


def has_pytorch():
    try:
        from backends import pytorch
    except:
        raise ImportError('Cannot load PyTorch support')


def pytorch_details():
    from backends import pytorch
    pytorch.details()
