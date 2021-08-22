from asyncio import tasks
from os import wait
from flask import Flask, jsonify

import asyncio, aiohttp, json

app = Flask(__name__)



async def call_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            return data


@app.route("/")
def main():
    urls = [
        "http://127.0.0.1:8000/first",
        "http://127.0.0.1:8000/second",
        "http://127.0.0.1:8000/third",
    ]
    loop = asyncio.new_event_loop()
    tasks = [loop.create_task(call_url(url)) for url in urls]
    done, _ = loop.run_until_complete(asyncio.wait(tasks, timeout=2))
    results_arr = []
    for result in done:
        results_arr.append(json.loads(result.result()))

    final_arr = []
    for item in results_arr:
        for item_dict in item:
            final_arr.append(item_dict)

    sorted_final_arr = sorted(final_arr, key=lambda k: k['id']) 
    return jsonify(sorted_final_arr)

@app.route("/first")
def first_file():
    with open('json_files/first.json') as first_file:
        data = json.load(first_file)
    return jsonify(data)


@app.route("/second")
def second_file():
    with open('json_files/second.json') as first_file:
        data = json.load(first_file)
    return jsonify(data)

@app.route("/third")
def third_file():
    with open('json_files/third.json') as first_file:
        data = json.load(first_file)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)