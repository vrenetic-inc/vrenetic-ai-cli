#!/usr/bin/python

def expression(inputs):
    return {
        "output": (1 - inputs[0])
    }

def expression_opencl(inputs):
    return """
        __kernel void sum(__global const float *a_g, __global const float *b_g, __global float *res_g) {
            int gid = get_global_id(0);
            res_g[gid] = a_g[gid] + b_g[gid];
        }
    """

