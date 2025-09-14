# Security Configuration for Django Project

## HTTPS & Redirects
- Enabled `SECURE_SSL_REDIRECT = True` to enforce HTTPS.
- Configured HSTS with `SECURE_HSTS_SECONDS = 31536000`, including subdomains and preload.

## Secure Cookies
- `SESSION_COOKIE_SECURE = True` and `CSRF_COOKIE_SECURE = True`.

## Secure Headers
- `X_FRAME_OPTIONS = "DENY"` prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents MIME sniffing.
- `SECURE_BROWSER_XSS_FILTER = True` activates browser XSS protection.

## Deployment
- Configured Nginx with SSL/TLS (Let's Encrypt).
- Redirects all HTTP traffic to HTTPS.
- Added extra headers for HSTS, clickjacking, XSS, and MIME sniffing protections.

## Review
- Debug is disabled in production.
- All traffic is forced through HTTPS.
- Potential improvement: Add a Content Security Policy (CSP) using `django-csp`.
