const sectionid_without = document.getElementById('container');
console.log(sectionid_without)

const sectionid_with = document.querySelector('#container');
console.log(sectionid_with)

const allLists = document.querySelectorAll('.second');
console.log(allLists)

const third_item = document.querySelector('ol .third');
console.log(third_item)

const secton_hello = document.createElement('section')
secton_hello.id = 'container'
secton_hello.innerText = 'Hello!'

const div_footer = document.querySelector('.footer');

div_footer.classList.add('main');
div_footer.classList.remove('main')
div_footer.remove()
console.log(div_footer)

const new_li = document.createElement('li')
new_li.innerText = 'four'
const ul_element = document.querySelector('ul')
ul_element.appendChild(new_li)
console.log(ul_element)


const ol = document.querySelector('ol li')
const ol_lis = ol.children
console.log(ol_lis)

for (lis of ol_lis){
    
}


