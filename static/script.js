function showEdit(button) {
    const task = button.closest(".task");
    const form = task.querySelector(".edit-form");

    if (form.style.display === "flex") {
        form.style.display = "none";
        button.textContent = "Edit";
    } else {
        form.style.display = "flex";
        button.textContent = "Cancel";
        form.querySelector("input").focus();
    }
}

setTimeout(function () {
    const messages = document.querySelectorAll(".message");
    messages.forEach(function (message) {
        message.style.display = "none";
    });
}, 4000);
