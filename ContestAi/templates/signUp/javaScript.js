// function handleSignUp(event) {
//   alert("catched");
//   event.preventDefault()
// }

// document.getElementById("btnSignUp").addEventListener("click", function(event){
//   event.preventDefault()
//   alert("catched");
// });

$(document).ready(function() {
//option A
const confirmPass = $("#inputConfirmPassword");
  confirmPass.blur(function(e){
      const pass = $("#inputPassword").val();
      const Cpass = confirmPass.val();
      if(pass!==Cpass){
        confirmPass.val('');
        alert("Confirm Password must be the same with Password ");
      }
  });
});

const checkSignUpbody = () => {};
