$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#contactModal .modal-content").html("");
        $("#contactModal").modal("show");
      },
      success: function (data) {
        $("#contactModal .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#contactModal").html(data.message);
          $("#contactModal").delay(1000).hide(400);
          setTimeout(function () { $("#contactModal").modal("hide"); }, 1200);
        }
        else {
          $("#contactModal .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */


  // Create book
  $(".js-contact-us").click(loadForm);
  $("#contactModal").on("submit", ".js-send-contact-form", saveForm);

});