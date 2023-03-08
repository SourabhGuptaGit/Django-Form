// function submitForm() {
//     // Get the first form with the name
//     // Usually the form name is not repeated
//     // but duplicate names are possible in HTML
//     // Therefore to work around the issue, enforce the correct index
//     var frm = document.getElementsByName('BR-form')[0];
//     frm.submit(); // Submit the form
//     frm.reset();  // Reset all form data
//     return false; // Prevent page refresh
//  }

// function submitForm() {
// document.getElementById("myForm").reset();
// }


// window.onbeforeunload = yourFunction() {
//     // put your code here
//     document.getElementById("myForm").reset();
//     }

function submitForm() {
    $('form[name="myForm"]').submit();
    $('input[type="text"], textarea').val('');
  }