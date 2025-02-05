import logging
import time

logger = logging.getLogger('django.request')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        # Log request details
        logger.info(f'Request: {request.method} {request.path} from {request.META.get("REMOTE_ADDR")}')
        if request.method in ['POST', 'PUT', 'PATCH']:
            logger.info(f'Request Body: {request.body}')
        
        response = self.get_response(request)
        
        # Calculate request duration
        duration = time.time() - start_time
        
        # Log response details
        logger.info(
            f'Response: {response.status_code} for {request.method} {request.path} '
            f'(took {duration:.2f}s)'
        )
        
        return response

    def process_exception(self, request, exception):
        logger.error(f'Exception during {request.method} {request.path}: {str(exception)}')