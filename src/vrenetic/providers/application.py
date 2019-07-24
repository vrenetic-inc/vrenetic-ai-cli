

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
        has_tensorflow()
        print('TensorFlow support: YES')
    except:
        print('TensorFlow support: NO')


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

    try:
        print()
        print('------- TensorFlow details -------')
        tensorflow_details()
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


def has_tensorflow():
    try:
        from backends import tensorflow
    except:
        raise ImportError('Cannot load TensorFlow support')

def tensorflow_details():
    from backends import tensorflow
    tensorflow.details()

