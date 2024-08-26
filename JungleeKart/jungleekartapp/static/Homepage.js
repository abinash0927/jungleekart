let v = 0;
let menu = document.querySelector(".fa-bars");
function MenuFunc(event) {
        let x = document.getElementById("navbarul");
        if(v == 0){
            x.style.display = "flex";
            v += 1;
            menu.classList.remove("fa-bars");
            menu.classList.add("fa-close");
        }
        else if(v == 1){
            x.style.display = "none";
            v -= 1;
            menu.classList.remove("fa-close");
            menu.classList.add("fa-bars");
        }
        
    }
let cart = document.getElementsByClassName("action");
for(let i = 0; i < cart.length; i++){
    cart[i].addEventListener("click", function(val){
        if (user != 'AnonyomousUser'){
            let product_id = val.target.getAttribute("data-product");
            let action = val.target.dataset.action
            var url = "/update_cart/"
            fetch(url,{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body:JSON.stringify({'productid':product_id,'action':action})
            })
            .then((response) =>{
                return response.json()
            })
            .then((data) =>{
                console.log('data:',data)
                location.reload()
            })
        }
    });

}

let fil = document.getElementsByClassName("but");
let inp = document.getElementsByClassName("sort");

function sortFilter(val){
    for(let j = 0; j < inp.length; j++){
        if (inp[j].checked){
            let sortby = inp[j].getAttribute("data-sortby");
            let url = "/products/"
            // fetch(url,{
            //     method: 'POST',
            //     headers: {
            //         'Content-Type': 'application/json',
            //         'X-CSRFToken': csrftoken,
            //     },
            //     body:JSON.stringify({'sortby':sortby})
            // })
            // .then((response) =>{
            //     return response.json()
            // })
            // .then((data) =>{
            //     console.log('data:',data)
            //     location.reload()
            // })
    }
    }
}

let ip = document.getElementsByClassName("expand");
let ep = document.getElementsByClassName("edpf");
for(let i = 0; i < ip.length; i++){
    ip[i].addEventListener("click",function(){
    // let y = this.nextElementSibling;
    // console.log(y.style.display == "none")
    if(ep[i].style.display == "flex"){
        ip[i].style.transform = "rotate(0deg)";
        ip[i].style.transition = "all .2s ease-in";
        ep[i].style.display = "none";
    } 
    else{
        ip[i].style.transform = "rotate(180deg)";
        ip[i].style.transition = "all .2s ease-in";
        ep[i].style.display = "flex";
    }
    });
}
let ex = document.getElementsByClassName("exp");
let pay = document.getElementsByClassName("pay");
for(let i = 0; i < ex.length; i++){
    ex[i].addEventListener("click",function(){
    // let y = this.nextElementSibling;
    console.log(pay[i].style.display);
    if(pay[i].style.display == "none"){
        ex[i].style.transform = "rotate(0deg)";
        ex[i].style.transition = "all .2s ease-in";
        pay[i].style.display = "flex";
    } 
    else{
        ex[i].style.transform = "rotate(180deg)";
        ex[i].style.transition = "all .2s ease-in";
        pay[i].style.display = "none";
    }
    });
}
function MyscrollTrans() {
    let x = document.querySelectorAll(".row");
    for(let i = 0; i < x.length; i++){
        var windowHeight = window.innerHeight;
        var elet = x[i].getBoundingClientRect().top;
        var elementVisible = 150;
        if(elet < windowHeight - elementVisible){
            x[i].classList.add("active");
        }
        else{
            x[i].classList.remove("active");
        }
    }
    let y = document.querySelectorAll(".anim");
    for(let i = 0; i < y.length; i++){
        var windowHeight = window.innerHeight;
        var elet = y[i].getBoundingClientRect().top;
        var elementVisible = 150;
        if(elet < windowHeight - elementVisible){
            y[i].classList.add("textani");
        }
        else{
            y[i].classList.remove("textani");
        }
    }
}
window.addEventListener("scroll",MyscrollTrans);

let r = 0;
let rail = document.querySelector(".nav-rail-but");
document.addEventListener("DOMContentLoaded",() => {
    rail.addEventListener("click",() => {
    let srt = document.querySelector(".sort-by");
    let butt = document.querySelector(".buttons");
    let nav_rail = document.querySelector(".nav-rail");
    if(r == 0){
        srt.style.display = "block";
        butt.style.display = "flex";
        nav_rail.style.width = "200px";
        // nav_rail.style.transition = "all .2s ease-in-out";
        r += 1;
        rail.classList.remove("fa-arrow-right");
        rail.classList.add("fa-close");
    }
    else if(r == 1){
        srt.style.display = "none";
        butt.style.display = "none";
        nav_rail.style.width = "30px";
        // nav_rail.style.transition = "all .2s ease-in-out";
        r -= 1;
        rail.classList.remove("fa-close");
        rail.classList.add("fa-arrow-right");

    }
});
});

let next = document.getElementById("next");
let prev = document.getElementById("prev");
let slideInd = 0;
let slides = document.getElementsByClassName("myslides");
let dot = document.getElementsByClassName("dot");

document.addEventListener("DOMContentLoaded",() => {
    next.addEventListener("click",function(){
        if(slideInd == slides.length-1){
            slideInd = 0;
            slides[slides.length-1].classList.remove("active");
            slides[slideInd].classList.add("active");
            dot[dot.length-1].classList.remove("active");
            dot[slideInd].classList.add("active");
            
        }
        else if(slideInd < slides.length){
            slides[slideInd].classList.remove("active");
            dot[slideInd].classList.remove("active");
            slides[++slideInd].classList.add("active");
            dot[slideInd].classList.add("active");
        }
    });
    prev.addEventListener("click",function(){
        if(slideInd == 0){
            slides[slideInd].classList.remove("active");
            dot[slideInd].classList.remove("active");
            slideInd = slides.length -1;
            slides[slideInd].classList.add("active");
            dot[slideInd].classList.add("active");
        }
        else if(slideInd > 0){
            dot[slideInd].classList.remove("active");
            slides[slideInd--].classList.remove("active");
            slides[slideInd].classList.add("active");
            dot[slideInd].classList.add("active");
        }
    });
});
document.addEventListener("DOMContentLoaded",function(){
    let d_l = 0;
    let xpx = document.querySelector(".ex");
    let all_d = document.querySelector(".sub_all_d");
    let pos = document.querySelector(".pro_but");
    xpx.addEventListener("click",function(){
    if(d_l == 0){
        xpx.style.transform = "rotate(180deg)";
        xpx.style.transition = "all .2s ease-in";
        all_d.style.display = "none";
        pos.style.position = "fixed"
        d_l += 1
    }
    else{
        xpx.style.transform = "rotate(0deg)";
        xpx.style.transition = "all .2s ease-in";
        all_d.style.display = "block";
        pos.style.position = "sticky"
        d_l = 0
    }
    });
});

document.querySelector(".signup").addEventListener("click",async () => {
    document.querySelector(".banner").style.display = "block";
    console.log("hello");
});