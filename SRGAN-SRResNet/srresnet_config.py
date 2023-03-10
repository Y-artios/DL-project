# Copyright 2022 Dakewe Biotech Corporation. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import random

import numpy as np
import torch
from torch.backends import cudnn

# Random seed to maintain reproducible results
random.seed(0)
torch.manual_seed(0)
np.random.seed(0)
# Use GPU for training by default
device = torch.device("cuda", 0)
# Turning on when the image size does not change during training can speed up training
cudnn.benchmark = True
# When evaluating the performance of the SR model, whether to verify only the Y channel image data
only_test_y_channel = True
# Model architecture name
g_arch_name = "srresnet_x4"
# Model arch config
in_channels = 3
out_channels = 3
channels = 64
num_rcb = 16
#num_blocks = 16
# Test upscale factor
upscale_factor = 4
# Current configuration parameter method
mode = "test"
# Experiment name, easy to save weights and log files
exp_name = "finetuning20epochs_SRResNet_x4-ImageNet"

if mode == "train":
    # Dataset address
    train_gt_images_dir = f"./data/Worldsat/train"

    test_gt_images_dir = f"./data/Worldsat/test/hr"
    test_lr_images_dir = f"./data/Worldsat/test/lr"

    gt_image_size = 96
    batch_size = 16
    num_workers = 4

    # The address to load the pretrained model
    pretrained_model_weights_path = f"./pretrained_models/SRResNet_x4-ImageNet-6dd5216c.pth.tar"

    # Incremental training and migration training
    resume_model_weights_path = f""

    # Total num epochs (1,000,000 iters)
    epochs = 15

    # loss function weights
    loss_weights = 1.0

    # Optimizer parameter
    model_lr = 1e-4
    model_betas = (0.9, 0.999)
    model_eps = 1e-8
    model_weight_decay = 0.0

    # How many iterations to print the training result
    train_print_frequency = 100
    valid_print_frequency = 1

if mode == "test":
    # Test data address
    lr_dir = f"./data/Worldsat/SRGAN/test/lr"
    sr_dir = f"./results/test/{exp_name}"
    gt_dir = f"./data/Worldsat/SRGAN/test/hr"

    model_weights_path = f"./results/SRResNet_finetuning20epochs_x4-ImageNet/g_best.pth.tar"
