import bap


async def main():
    service = bap.Bap('<ad provider api key>')
    # sending telegram update data
    needHandle = await service.handle_update(
        {
            'update_id': 123,
            # ...
        }
    )

    # or if your advertisement mode is set to manual you can mark ad placement in your code by calling:
    await service.send_advertisement(
        {
            'update_id': 123,
            # ...
        }
    )
