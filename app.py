from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "ad96171a3f768a4396124d737403ac02"

def get_weather(city):


             
