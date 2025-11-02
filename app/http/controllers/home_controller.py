from larapy.http import Controller, Request, Response


class HomeController(Controller):
    
    def index(self, request: Request) -> Response:
        return self.view('welcome')
    
    def dashboard(self, request: Request) -> Response:
        user = request.user()
        return self.view('dashboard', {'user': user})
