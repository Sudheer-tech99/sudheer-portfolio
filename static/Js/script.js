/*
function changeProjectImage(thumbnail) {
    const mainImage = document.getElementById("main-project-image");

    if (!mainImage || !thumbnail) return;

    mainImage.src = thumbnail.src;
    mainImage.alt = thumbnail.alt;

    const thumbnails = document.querySelectorAll(
        ".project-visual.gallery .project-thumbnails img"
    );

    thumbnails.forEach((image) => {
        image.classList.remove("active");
    });

    thumbnail.classList.add("active");
}
*/

function changeImage(thumbnail) {
    const mainImage = document.getElementById("mainImage");

    mainImage.src = thumbnail.src;
    mainImage.alt = thumbnail.alt;
}
