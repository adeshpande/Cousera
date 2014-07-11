
function checkprimenumber(n){
    for (c=2; c<=n - 1; c++){
        if ( n%c == 0 ){
            return false;
                        }
            return true;
                        }
}

function printprimenumber(number){
    if(checkprimenumber(number) == true){
        document.write(number);
        }else{
        document.write(number);
        }
}

function printnumbers(range){
    for (i=1; i<=range; i++){
         printprimenumber(i);
    }
}

var maxnumber = 100;
printnumbers(maxnumber);
