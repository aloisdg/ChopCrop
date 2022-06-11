# ChopCrop
ChopCrop is a glued python script to remove background then crop of images 


You need python3.9 or above.

## Getting started

Start by `pip install rembg pillow glob`. If you have a traceback on `Downloading u2net.pth to /home/aloisdg/.u2net` download the model manually from [Google Drive](https://docs.google.com/uc?export=download&id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ) and save it to `~/.u2net/u2net.pth` it should work.

Then download [chopcrop](https://raw.githubusercontent.com/aloisdg/ChopCrop/main/chopcrop.py) and finally `python chopcrop.py "*.jpg"`.

## License

GPL3
