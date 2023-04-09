//Return the number (count) of vowels in the given string.

//We will consider a, e, i, o, u as vowels for this Kata (but not y).

//The input string will only consist of lower case letters and/or spaces.


function getCount(str) {
    str1 = ""
    for (let i = 0; i < str.length; i++) {
        const element = str[i];
      
        if(element == 'a' || element == 'e'  || element == 'i' || element == 'o' || element == 'u' ){
            str1 +=element
        }
    }
    return str1.length

}

  getCount("testing")