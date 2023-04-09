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