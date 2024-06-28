import asyncio
from pyppeteer import launch
from pyppeteer.browser import BrowserContext

async def main():
    print('launching')
    browser = await launch(
        headless=False,
        args=[
            #'--headless',
            '--no-sandbox',
            '--disable-gpu'
        ],
        autoClose=False,
        executablePath='/snap/bin/chromium'
    )
    print('new page')
    page = await browser.newPage()
    print('goto')
    await page.goto('https://www.ignitioncasino.eu/poker')
    print('create session')
    cdp = await page.target.createCDPSession()
    raw_context = await cdp.send('Target.createBrowserContext')
    print(raw_context)
    print('network enable')
    await cdp.send('Network.enable')
    print('page enable')
    await cdp.send('Page.enable')
    context = BrowserContext(browser, raw_context['browserContextId'])
    new_page = await context.newPage()
    await cdp.detach()
    await browser.disconnect()
    

    def printResponse(response):
        print(response)

    cdp.on('Network.webSocketFrameReceived', printResponse)  # Calls printResponse when a websocket is received
    cdp.on('Network.webSocketFrameSent', printResponse)  # Calls printResponse when a websocket is sent
    #await asyncio.sleep(100)


asyncio.get_event_loop().run_until_complete(main())
