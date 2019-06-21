from __future__ import division, absolute_import, print_function

try:
    import pyopencl as cl
    import pyopencl.characterize.performance as perf
    from six.moves import range
    import numpy as np
    import pprint
except Exception as error:
    raise Exception('OpenCL not supported')


def run(kernel_code):
    context = get_default_context()
    program = get_program(context, kernel_code)
    queue = get_queue(context)

    a_np = np.random.rand(5000000).astype(np.float32)
    b_np = np.random.rand(5000000).astype(np.float32)

    mf = cl.mem_flags
    a_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
    b_g = cl.Buffer(context, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

    res_g = cl.Buffer(context, mf.WRITE_ONLY, a_np.nbytes)

    program.sum(queue, a_np.shape, None, a_g, b_g, res_g)

    res_np = np.empty_like(a_np)
    cl.enqueue_copy(queue, res_np, res_g)

    pprint.pprint(res_np)
    # print(res_g)
    # raise Exception('Not implemented')


def get_program(context, kernel_code):
    return cl.Program(context, kernel_code).build()


def get_queue(context):
    return cl.CommandQueue(context)


def get_default_context():
    platform = cl.get_platforms()[0]
    device = platform.get_devices()[0]
    return cl.Context([device])


def details():
    platforms = cl.get_platforms()

    for platform in platforms:
        print(platform.name)
        print(" - Profile: ", platform.profile)
        print(" - Version: ", platform.version)
        print(" - Devices: ")
        devices = platform.get_devices()
        for device in devices:
            print("   - ", device.name)


def performance_test():
    ctx = cl.create_some_context()

    prof_overhead, latency = perf.get_profiling_overhead(ctx)
    print("command latency: %g s" % latency)
    print("profiling overhead: %g s -> %.1f %%" % (
            prof_overhead, 100*prof_overhead/latency))
    queue = cl.CommandQueue(
            ctx, properties=cl.command_queue_properties.PROFILING_ENABLE)

    print("empty kernel: %g s" % perf.get_empty_kernel_time(queue))
    print("float32 add: %g GOps/s" % (perf.get_add_rate(queue)/1e9))

    for tx_type in [
            perf.HostToDeviceTransfer,
            perf.DeviceToHostTransfer,
            perf.DeviceToDeviceTransfer]:
        print("----------------------------------------")
        print(tx_type.__name__)
        print("----------------------------------------")

        print("latency: %g s" % perf.transfer_latency(queue, tx_type))
        for i in range(6, 31, 2):
            bs = 1 << i
            try:
                result = "%g GB/s" % (perf.transfer_bandwidth(queue, tx_type, bs)/1e9)
            except Exception as e:
                result = "exception: %s" % e.__class__.__name__
            print("bandwidth @ %d bytes: %s" % (bs, result))

