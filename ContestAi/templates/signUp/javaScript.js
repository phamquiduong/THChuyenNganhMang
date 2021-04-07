$(document).ready(function () {
  const confirmPass = $("#inputConfirmPassword");
  confirmPass.blur(function (e) {
    const pass = $("#inputPassword").val();
    const Cpass = confirmPass.val();
    if (pass !== Cpass) {
      confirmPass.val("");
      alert("Confirm Password must be the same with Password ");
    }
  });
});
