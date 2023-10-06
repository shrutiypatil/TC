document.addEventListener("DOMContentLoaded", function () {
    const feedbackForm = document.getElementById("feedback-form");

    feedbackForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        const feedbackData = {
            name: name,
            email: email,
            message: message,
        };

        fetch('/submit_feedback', {  // Send the request to the same origin as your frontend
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(feedbackData),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // You can perform actions here based on the response
        })
        .catch(error => {
            console.error('Error:', error);
        });

        feedbackForm.reset();
    });
});
