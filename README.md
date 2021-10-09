# Projeto_de_Previsao_do_Tempo


####Bibliotecas utilizadas

import pandas as pd
import numpy as np
import xmltodict
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from urllib.request import urlopen
from sqlite3 import Error
import json
import os
from PIL import Image
import requests
from flask import Flask, render_template, request

####É necessário instalar as seguintes bibliotecas 
pip install Flask
pip install xmltodict
pip install matplotlib

#### EXECUTE o arquivo app.py para rodar a API
