
var p = document.querySelector("#btn");

var sq = document.querySelectorAll('td');

function del() {
    for(var i=0;i<sq.length;i++)sq[i].textContent='';
      
    }


p.addEventListener('click', del);

function input(){
    if(this.textContent === '')this.textContent = 'X', this.style.color = "red";
      
      
    else if (this.textContent === 'X')this.textContent = 'O', this.style.color = "#5eff00";
     
    else  this.textContent = '';
     
    
}


for (var i =0; i< sq.length; i++){
    sq[i].addEventListener('click', input);
}

          
        
    






