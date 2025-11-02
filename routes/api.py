from larapy.routing import Router

router = Router()

router.prefix('/api').group(lambda: [
    router.get('/health', lambda: {'status': 'ok'}),
])
