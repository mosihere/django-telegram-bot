from rest_framework.throttling import SimpleRateThrottle



class TelegramUserThrottle(SimpleRateThrottle):
    scope = 'telegram_user'

    def get_cache_key(self, request, view):
        user_id = request.headers.get("X-Telegram-User-ID")
        if not user_id:
            return None  # No user header, do not throttle
        return f"throttle_{self.scope}_{user_id}"