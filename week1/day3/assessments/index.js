// const checkDetails = function(event){

//         event.preventDefault();


//         const age = document.getElementById("age").value
//         const password = document.getElementById("password").value

//         const Age=Number(age)

//         if(Age<=0 || Age>=100){
//             alert("The age must be greater than 0 and less than 100")
//             return;
//         }

//         if (password.length < 6) {
//             alert("Password must contain at least 6 characters")
//             return;
//         }


//         alert("Regiration successfull")
        
//         document.getElementById("form").reset()
//     }

// document.getElementById("form").addEventListener("submit",checkDetails)


$(document).ready(function(){
    $("form").on("submit",function(event){

        event.preventDefault()

        const age=Number($("age").val())
        const password=$("password").val()
        if(age<=0 || age>=100){
            alert("Age is invalid")
            return
        }
        if(password.length < 6){
            alert("Password is invalid")
            return
        }

        alert("Registered")

        $("form")[0].reset();
    })
});