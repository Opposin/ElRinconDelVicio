document.getElementById("myButton").onclick = function () {
    location.href = "https://store.steampowered.com/app/70/HalfLife/";
};

window.addEventListener("scroll", function(){
    var header = document.querySelector("header")
    header.classList.toggle("sticky", window.scrollY > 15)
})
