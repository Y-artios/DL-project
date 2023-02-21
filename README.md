# DL-project
This repository contains our code for the MVA Deep Learning course project.
The code is based on the op-for-op PyTorch reimplementation of [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://arxiv.org/abs/1609.04802v5) which can be found [here](https://github.com/Lornatang/SRGAN-PyTorch#how-test-and-train).

## Pretrained weights
- [Google Drive](https://drive.google.com/drive/folders/17ju2HN7Y6pyPK2CC_AqnAfTOe9_3hCQ8?usp=sharing)

## Data

The WorldSat dataset can be downloaded and preprocessed by running `Downloading the data.ipynb` and `Preprocessing_the_database.ipynb` in `Data` and then `split_dataset.ipynb` in `SRGAN-SRResNet/scripts`. 
The notebook `create lr samples.ipynb` is used to create the low-resolution samples for the test.


## How to Test and Train

Both training and testing can be done by modifying the `srresnet_config.py` file and `srgan_config.py` file in `SRGAN-SRResNet` and then running either `train_srgan.py`, `train_srresnet.py`, `test_srgan.py` or `test_srresnet.py` depending on what we want.

## Authors
- Youssef Attia El Hili
- Safwan Labbi
