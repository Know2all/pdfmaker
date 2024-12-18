import uvicorn
import os
import base64
import asyncio
from flask import Flask, request, jsonify
from asgiref.wsgi import WsgiToAsgi
from pyppeteer import launch

app = Flask(__name__)

async def clock():
    await asyncio.sleep(5)
    return "alarmed"

@app.route('/test', methods=['GET'])

async def test():
    alarm = await clock()
    return jsonify({'status': 'ok', 'alarm': alarm})

async def generate_pdf_base64(url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url, {'waitUntil': 'networkidle2'})

    pdf_bytes = await page.pdf({
        'format': 'A4',
        'printBackground': True,
    })

    await browser.close()
    
    return base64.b64encode(pdf_bytes).decode('utf-8')

@app.route('/pdf_generate', methods=['POST'])
async def generate_pdf_from_url():
    url = request.form.get('url')
    try:
        if not url:
            return jsonify({'error': 'No URL provided'}), 400
        
        pdf_base64 = await generate_pdf_base64(url)
        return jsonify({'pdf': pdf_base64})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def hello():
    return 'Welcome To PDF Generator'

asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    uvicorn.run(asgi_app, host="0.0.0.0", port=3500)
