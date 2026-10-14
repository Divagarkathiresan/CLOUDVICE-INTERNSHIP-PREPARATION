let num=0
const pi=3.14

const list=[1,2,3,4]
list[0]=99
list.push(5)
console.log(list[0])
console.log(num)

printName('Diva')

const Name = function(){
    return "shree"
}
Name()


function printName(name){
    console.log(name)
}

printName("Divagar")


// call back functions
const getCollege = (Name) => {
    console.log(Name + " Divagar")
}

getCollege(Name())