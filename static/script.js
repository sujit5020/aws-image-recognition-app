document.getElementById("uploadForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    let formData = new FormData(this);
    let response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    let result = await response.json();
    let resultsDiv = document.getElementById("results");

    if (result.error) {
        resultsDiv.innerHTML = `<p style="color:red">${result.error}</p>`;
    } else {
        resultsDiv.innerHTML = "<h3>Detected Labels:</h3><ul>" +
            result.labels.map(label => `<li>${label.Name} (${label.Confidence}%)</li>`).join("") +
            "</ul>";
    }
});
