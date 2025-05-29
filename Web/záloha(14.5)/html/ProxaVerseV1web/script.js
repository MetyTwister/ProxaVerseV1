
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const password = loginForm.password.value;

    if (password === "user") {
        location.replace("index2.html")
    } else {
        location.reload();
        alert("Nesprávné heslo")
    }
})