// function filterOutOdds() {
//     var nums = Array.prototype.slice.call(arguments);
//     return nums.filter(function(num) {
//       return num % 2 === 0
//     });
//   }

const filterOutOdds = ( ...nums ) => (nums.filter(num => num % 2 === 0));

// findMin(1,4,12,-3) // -3
// findMin(1,-1) // -1
// findMin(3,1) // 1

const findMin = ( ...nums ) => (nums.reduce((min, current_val) => current_val < min ? current_val:min));

// mergeObjects({a:1, b:2}, {c:3, d:4}) // {a:1, b:2, c:3, d:4}


const mergeObjects = (obj1,obj2) => { 
    const mergedobj = {...obj1, ...obj2}
    return mergedobj;
}

// doubleAndReturnArgs([1,2,3],4,4) // [1,2,3,8,8]
// doubleAndReturnArgs([2],10,4) // [2, 20, 8]

const doubleAndReturnArgs = (arr, ...elements) => {
    const d_vals = [...elements].map(val => val * 2);
    combined_arr = [...arr, ...d_vals]
    return combined_arr;
}

/** remove a random element in the items array
and return a new array without that item. */

const removeRandom = (items) => {
    let random_index = Math.floor(Math.random() * items.length);
    return [...items.slice(0, idx), ...items.slice(idx + 1)];
  }




/** Return a new array with every item in array1 and array2. */

const extend = (array1, array2) => {
    return [...array1, ...array2]

}

/** Return a new object with all the keys and values
from obj and a new key/value pair */

const addKeyVal = (obj, key, val) => {
        return { ...obj , key:val}
}


/** Return a new object with a key removed. */

function removeKey(obj, key) {
    let newObj = { ...obj }
    delete newObj[key]
    return newObj;
  
}


/** Combine two objects and return a new object. */

const combine = (obj1, obj2) => {
        return { ...obj1, ...obj2 };
  }

/** Return a new object with a modified key and value. */

function update(obj, key, val) {
        return {...obj, obj[key]:val}
}
