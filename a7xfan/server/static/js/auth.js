let username = document.getElementById('user');
let email = document.getElementById('mail');
let password = document.getElementById('pass');
let retype_pass = document.getElementById('retype-pass');

function register() {
   if(username.value == '' && email.value == '' && password.value == '' && retype_pass.value == '') {
     alert('No Value');
     return false;
   }
   if(username.value == '') {
     alert('Enter a Username');
     return false;
   }
   if(email.value == '') {
     alert('Enter a Email');
     return false;
   }
   if(password.value == '') {
     alert('Enter a Password');
     return false;
   }
   if(retype_pass.value == '') {
     alert('Retype_Password Must Enter');
     return false;
   }
   if(password.value.length < 10) {
     alert('Password Atleast 10 Digits');
     return false;
   }
   if(password.value !== retype_pass.value) {
     alert('Password Not Matched');
     return false;
   }
   if(email.value.indexOf('@') == -1) {
     alert('Missing @ in Email');
     return false;
   }
}
function login() {
    if(username.value == '' && password.value == '') {
      alert('Enter username and password');
      return false;
    }
    if(username.value == '') {
      alert('Enter a username');
      return false;
    }
    if(password.value == '') {
      alert('Enter a password');
      return false;
    }
}