self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open('flask-pwa-cache').then((cache) => {
            return cache.addAll([
                '/',
                '/static/css/style.css',
                '/static/js/main.js',
                'static/images/sitelogo.jpg'
            ]);
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((response) => {
            return response || fetch(event.request);
        })
    );
});
