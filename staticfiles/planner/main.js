function openNav() {
  document.getElementById("leftnav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";

}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("leftnav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

function myFunction() {
  var dots = document.getElementById("dots_"+id);
  var moreText = document.getElementById("more_"+id);
  var btnText = document.getElementById("myBtn_"+id);

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}

var coll = document.getElementById("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

function change(priority){
  if (priority == "high"){
    document.getElementById("priority").selectedIndex = 0;
  }
  else if (priority =='medium'){
    document.getElementById("priority").selectedIndex = 1; 
  }
  else {
    document.getElementById("priority").selectedIndex = 2; 
  }
}

// Close the dropdown menu if the user clicks outside of it
// var today = new Date();
// var date_form = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
// document.getElementById('dates').value=date_form;