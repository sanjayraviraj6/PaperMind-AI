const dropZone = document.getElementById("dropZone");
const fileInput = document.getElementById("pdf_files");
const selectedFiles = document.getElementById("selectedFiles");

// Open file picker
dropZone.addEventListener("click", () => {
    fileInput.click();
});

// Show selected files
fileInput.addEventListener("change", () => {
    displayFiles(fileInput.files);
});

// Drag over
dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("dragover");
});

// Drag leave
dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("dragover");
});

// Drop
dropZone.addEventListener("drop", (e) => {

    e.preventDefault();

    dropZone.classList.remove("dragover");

    fileInput.files = e.dataTransfer.files;

    displayFiles(fileInput.files);

});

// Display selected filenames
function displayFiles(files) {

    selectedFiles.innerHTML = "";

    for (const file of files) {

        const li = document.createElement("li");

        li.textContent = "📄 " + file.name;

        selectedFiles.appendChild(li);

    }

}