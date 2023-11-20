#This code is intended to work with google colab

import torch

class Args:
    pass

def parse_args():
    """
    Parse input arguments
    """
    args = Args()

    args.training = "yes"
    args.label_marker = "durative"
    args.data_path = "/content/drive/MyDrive"
    #args.transformer_model = "bert-base-multilingual-cased"
    #args.model_type = "bert-base-multilingual-cased"
    args.transformer_model = "indolem/indobert-base-uncased"
    args.model_type = "indolem/indobert"
    args.num_epochs = 16
    args.batch_size = 32
    args.verb_segment_ids = "yes" 
    args.freeze_layer_count = -1

    return args
