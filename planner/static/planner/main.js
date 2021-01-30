/* Aimee Maredia 
   Mr. Moore
   ICS4U
   Jan, 29th 2021
   main.js field for some java methods used for html manipulated */

/* method to open left side bar */
function openNav() {
  document.getElementById("leftnav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}
/* method to close the left side bar */
function closeNav() {
  document.getElementById("leftnav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}
/* function to change preselected priority field in input form*/
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
