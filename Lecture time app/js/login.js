// Define a simple array to store user credentials
const users = [
    { username: "1NACOS", password: "1NAIJA!" }
    // Add more users as needed
];

function checkLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Check if the provided username and password match any user in the array
    const user = users.find(user => user.username === username && user.password === password);

    if (user) {
        window.location.href = "home.html";
        
        return false;
    } else {
        alert("Invalid username or password");

        return false;
    }
}
