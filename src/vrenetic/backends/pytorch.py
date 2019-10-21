try:
    import torch
    from torch.jit import script, trace
    import torch.nn as nn
    from torch import optim
    import torch.nn.functional as F
except Exception as error:
    raise Exception('PyTorch not supported')


def details():
    print("CUDA:", torch.cuda.is_available())

