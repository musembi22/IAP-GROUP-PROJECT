// Display current date and time in the console
document.addEventListener("DOMContentLoaded", () => {
    console.log("Custom JavaScript loaded.");

    // Alert for RSVP buttons
    const rsvpButtons = document.querySelectorAll(".btn-success");
    rsvpButtons.forEach(button => {
        button.addEventListener("click", () => {
            alert("Thank you for RSVPing! 🎉");
        });
    });

    // Add dynamic highlighting on focus for form fields
    const formInputs = document.querySelectorAll("input, textarea");
    formInputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.style.backgroundColor = "#fffbe6";
        });
        input.addEventListener("blur", () => {
            input.style.backgroundColor = "white";
        });
    });
});
