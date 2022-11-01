import logging
import asyncio

from aiocoap import *

ESP32_IP = "192.168.3.72"

TEST = "GET"
TEST = "PUT"

logging.basicConfig(level=logging.INFO)

async def get():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://'+ ESP32_IP +'/Espressif')

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r'%(response.code, response.payload))

async def put():
    context = await Context.create_client_context()

    await asyncio.sleep(2)

    payload = b"The quick brown fox jumps over the lazy dog.\n"
    request = Message(code=PUT, payload=payload, uri='coap://'+ ESP32_IP +'/Espressif')

    response = await context.request(request).response

    print('Result: %s\n%r'%(response.code, response.payload))

if __name__ == "__main__":
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  print("*** GET ***")
  asyncio.run(get())
  print("*** PUT ***")
  asyncio.run(put())
  print("*** GET ***")
  asyncio.run(get())

