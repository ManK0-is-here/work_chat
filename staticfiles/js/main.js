
function toggleMenu() {
    let panel = document.getElementById("menu-panel");
    panel.style.display = (panel.style.display === "block") ? "none" : "block";
}

document.addEventListener("click", function(event) {
    const menu = document.getElementById("menu-panel");
    const btn = document.querySelector(".menu-btn");
    if (menu && !menu.contains(event.target) && !btn.contains(event.target)) {
        menu.style.display = "none";
    }
});
