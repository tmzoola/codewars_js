// You are going to be given a word. 
//Your job is to return the middle character of the word. 
//If the word's length is odd, return the middle character. 
//If the word's length is even, return the middle 2 characters.
let num1 = String(prompt("Enter num1:"));
bir=0
ikki = 0
for (const num of num1) {
  if(num == "1"){
    bir= bir+1
  }else{
    ikki=ikki+1
  }
  
}
if(bir>ikki){
  console.log(ikki);
}else{
  console.log(bir);
}
