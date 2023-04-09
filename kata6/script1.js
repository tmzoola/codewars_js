
//Create a function isAlt() that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) 
//and consonants are in alternate order.
//For Example
//isAlt("amazon")
// true
//isAlt("apple")
// false
//isAlt("banana")
// true

function isAlt(word) {

    function vowel(c) {
      let vow = ["a", "e", "o", "i", "u"];
      return vow.includes(c);
    }
  
    for (i = 0; i < word.length - 1; i++) {
      if (vowel(word[i]) == vowel(word[i + 1])) {
        return false;
      }
    }
    return true;
  }
  
  console.log(isAlt('apple'));
  console.log(isAlt('amazon'));