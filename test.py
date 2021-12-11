from flask import Flask, request, jsonify
import requests
import json
url = 'http://localhost:5000/'

def test_hello_world():
  json_str = requests.get(url).content
  json_obj = json.loads(json_str)
  assert json_obj["msg"], "hello world!"

if __name__ == "__main__":
  test_hello_world()
  print("Everything passed")

