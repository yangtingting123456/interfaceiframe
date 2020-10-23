#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: demo_08.py
# @time: 2020/9/20 2:19 下午

# https://c-ssl.duitang.com/uploads/item/201606/02/20160602205156_NwG25.jpeg

from PIL import Image
from io import BytesIO
import requests

resonse = requests.get(url="https://c-ssl.duitang.com/uploads/item/201606/02/20160602205156_NwG25.jpeg")
img = Image.open( BytesIO(resonse.content) )
img.save('../data/a.jpeg')
