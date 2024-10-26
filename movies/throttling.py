from rest_framework.throttling import SimpleRateThrottle



class MovieLinkThrottle(SimpleRateThrottle):
    scope = 'movie_link_requests'

    def get_cache_key(self, request, view):
        user_id = request.headers.get("X-Telegram-User-ID")

        if not user_id:
            return None
        
        return f"throttle_{self.scope}_{user_id}"


class MovieSearchThrottle(SimpleRateThrottle):
    scope = 'movie_search'

    def get_cache_key(self, request, view):
        user_id = request.headers.get("X-Telegram-User-ID")

        if not user_id:
            return None
        
        return f"throttle_{self.scope}_{user_id}"