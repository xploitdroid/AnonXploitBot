from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("XploitBots")




# Developer Ankit 
# Don't Remove Credit 🥺
# Telegram Channel @XploitBots
# Backup Channel @XploitdroidBots
# Developer @Xploitdroid
