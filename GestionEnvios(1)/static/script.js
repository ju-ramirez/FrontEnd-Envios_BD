const header = document.querySelector("header")
const mainTitle = document.querySelector(".who-are-we")

options = {}
const observer = new IntersectionObserver(function (entries, observer) {
    entries.forEach(entry => {
        if(entry.isIntersecting) {
            header.classList.add('nav-white')
        } else {
            header.classList.remove('nav-white')
        }
    })
}, options)


observer.observe(mainTitle);