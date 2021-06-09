var clickMe = document.getElementById('clickMe');
var heading = document.getElementById('homeHeading');

var count = 0;


clickMe.onclick = () => {
    count = count+1;

    if(count%2==0){
        heading.innerHTML = "Even"
    }
    else{
        heading.innerHTML = "Odd"
    }

}