// MOBILE MENU 

function OpenCloseMenu() {
    let menu = document.querySelector(".mobile-menu");
    let menuIcon = document.querySelector("#menu-icon");
    menu.classList.toggle("active");
    if (menu.classList.contains("active")) {
        menuIcon.src = './src/cross.svg'
    } else {
        menuIcon.src = './src/menu-hamburger.svg'
    }
}