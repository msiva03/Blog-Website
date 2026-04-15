
class SetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("one time configuration")

    def __call__(self, request):
        print("before view execution")
        response = self.get_response(request)
        print("after view execution")
        return response
    