def preprocess_input(text: str):
    # Dummy preprocessing for illustration
    import torch
    return torch.tensor([ord(c) for c in text]).unsqueeze(0)

def postprocess_output(tensor):
    # Dummy postprocessing for illustration
    return ''.join([chr(int(x)) for x in tensor.squeeze().tolist()])
