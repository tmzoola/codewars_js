function high(x){
    var alphabet = [ '','a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y',
    'z' ];

    arr=[]
    for (y in x) {
        a = x[y]
        
        sum = 0
        for (let i = 0; i < a.length; i++) {
         var element = a[i];
         sum+=alphabet.indexOf(element)
        }
        arr.push(sum)
       arr.push( a ) 
    }

    var largest = arr[0];
    for (var i = 0; i < arr.length; i++) {
        if (largest < arr[i] && typeof(largest == 'number') ) {
        largest = arr[i];
         }
    }
    return arr[arr.indexOf(largest) +1];
}

high(['abad','sada'])