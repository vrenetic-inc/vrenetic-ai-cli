try:
    import tensorflow as tf
except Exception as error:
    raise Exception('TensorFlow not supported')


def details():
    print("CUDA:", tf.test.is_gpu_available())

