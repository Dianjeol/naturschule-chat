// Ensure desktop notification permission is requested on first user interaction
// when not yet decided, so Campai Chat alerts work out of the box.
(function () {
  try {
    if (typeof window === 'undefined' || !('Notification' in window)) {
      return;
    }
    if (Notification.permission !== 'default') {
      return;
    }

    var requested = false;
    var requestOnce = function () {
      if (requested || Notification.permission !== 'default') {
        return;
      }
      requested = true;
      window.removeEventListener('click', requestOnce, true);
      window.removeEventListener('keydown', requestOnce, true);
      try {
        Notification.requestPermission().catch(function () {});
      } catch (_) {}
    };

    window.addEventListener('click', requestOnce, true);
    window.addEventListener('keydown', requestOnce, true);
  } catch (_) {}
})();
