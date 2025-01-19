// Arreglo de imágenes y descripciones
const images = [
    { src: "/static/img/gallery/1.jpeg", caption: "Descripción de la imagen 1" },
    { src: "/static/img/gallery/2.jpg", caption: "Descripción de la imagen 2" },
    { src: "/static/img/gallery/3.jpg", caption: "Descripción de la imagen 3" },
    // Agrega más objetos de imagen y descripción aquí
];

let currentIndex = 0;

function showImage(index) {
    const imageElement = document.getElementById("slider-image");
    const captionElement = document.getElementById("caption");

    // Actualiza la imagen y la descripción
    imageElement.src = images[index].src;
    captionElement.textContent = images[index].caption;
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length; // Mueve al siguiente índice
    showImage(currentIndex);
}

function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length; // Mueve al índice anterior
    showImage(currentIndex);
}

// Muestra la primera imagen al cargar la página
showImage(currentIndex);
