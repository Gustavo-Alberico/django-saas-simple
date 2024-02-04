document.addEventListener('DOMContentLoaded', function () {
  var alerts = document.querySelectorAll('.alert-dismissible');
  var alertTimeout = 5000;

  alerts.forEach(function (alert) {
    setTimeout(function () {
      var alertInstance = new bootstrap.Alert(alert);
      alertInstance.close();
    }, alertTimeout);
  });
});
