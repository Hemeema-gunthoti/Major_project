<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $question = htmlspecialchars($_POST['question']);

    // Send a confirmation message back
    echo "Thank you, $name! Your question has been submitted successfully.";
} else {
    echo "Invalid request. Please submit the form.";
}
?>
