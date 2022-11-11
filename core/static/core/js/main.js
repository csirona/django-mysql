// Get the modal
var modal = document.getElementsByClassName("modal");
                          
// Get the image and insert it inside the modal - use its "alt" text as a caption
var imgs = document.querySelectorAll(".myBtn");

// get all images and add an event listener, event target will be the clicked one
imgs.forEach(img=>img.addEventListener("click",
  function () {
    //modal[1].style.display = "block";
    console.log(modal[2])
 }
))

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
                     
// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
        modal.style.display = "none";
        }