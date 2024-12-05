document.getElementById("form").addEventListener("submit", function (e) {
    e.preventDefault();
    const input = document.getElementById("Input").value.trim();
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = ""; 

    if (!input) {
        resultDiv.innerHTML = "<p class='error'>Input cannot be empty!</p>";
        return;
    }

    fetch("/convert/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ text: input }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p class='error'>${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `<p class='success'>Result: ${data.result}</p>`;
            }
        });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
