// let modal = document.getElementById("myModal");
//   let i;
//   let j;
//   let k;

//   // Get image
//   let img = document.getElementsByClassName("myImg");
//   let myName = document.getElementsByClassName("myName");
//   let myDesc = document.getElementsByClassName("myDesc");
//   let modalImg = document.getElementById("showImg");
//   let modalName = document.getElementById("imgName");
//   let modalDesc = document.getElementById("imgDesc");

//   // Loop through images
//   for (i = 0; i < img.length; i++) {
//     img[i].onclick = function () {
//       modal.style.display = "block";
//       modalImg.src = this.src;
//       modalName.innerHTML = this.parentElement.getElementsByClassName('myName')[0].innerHTML;
//       modalDesc.innerHTML = this.parentElement.getElementsByClassName('myDesc')[0].innerHTML;
//     }
//   }

var modal = document.querySelectorAll('.modal')

var btn = document.querySelectorAll('.myBtn')

var span = document.getElementsByClassName("close")[0];
function openModal(i) {
    modal[i].style.display = 'block';
    span.style.display = 'block';
}
function closeModal(){
    modal.style.display = 'none';
    span.style.display = 'none';
}

for (i=0; i < btn.length; i++){


    btn[1].addEventListener('click',openModal(i))
    console.log(modal[i])
}

span.onclick = closeModal;