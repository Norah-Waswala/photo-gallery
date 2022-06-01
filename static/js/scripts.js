function myFunction() {
    /* Get the text field */
    var copyUrl = document.getElementById("myInput");
  
    /* Select the text field */
    copyUrl.select();
    copyUrl.setSelectionRange(0, 99999); /* For mobile devices */
  
    /* Copy the text inside the text field */
    navigator.clipboard.writeText(copyUrl.value);
    
    /* Alert the copied text */
    alert("Copied the text: " + copyUrl.value);
  }