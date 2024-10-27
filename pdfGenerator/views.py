import base64
import asyncio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pyppeteer import launch

async def clock():
    await asyncio.sleep(20)
    return "alarmed"

async def test(request):
    alarm = await clock()
    return JsonResponse({'status':'ok','alarm':alarm})

async def generate_pdf_base64(url):
    browser = await launch(headless=True,executablePath='C:/Program Files/Google/Chrome/Application/chrome.exe')
    page = await browser.newPage()
    await page.goto(url, {'waitUntil': 'networkidle2'})

    pdf_bytes = await page.pdf({
        'format': 'A4',
        'printBackground': True,
    })

    await browser.close()
    
    return base64.b64encode(pdf_bytes).decode('utf-8')

@csrf_exempt
async def generate_pdf_from_url(request):
    url = request.POST.get('url') 
    try:
        if not url:
            return JsonResponse({'error': 'No URL provided'}, status=400)
        pdf_base64 = await generate_pdf_base64(url)
        return JsonResponse({'pdf': pdf_base64})
    except Exception as e:
        return JsonResponse({'error':str(e)}, status=500,safe=True)