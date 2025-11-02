from larapy.routing import Router
from app.http.controllers.home_controller import HomeController

router = Router()

router.get('/', [HomeController, 'index']).name('home')

router.middleware(['auth']).group(lambda: [
    router.get('/dashboard', [HomeController, 'dashboard']).name('dashboard'),
])
