{% extends "base.html" %}

{% block head %} 
<title>Home Page</title>
{% endblock %}

{% block body %} 
<h1>Welcome to Home Page</h1>
<form action="process/process-index.php" method="POST" enctype="multipart/form-data">  
    <select name="selectedOption" id="selectedOption">
        <option value="default" hidden>--Choose Save Location--</option>
        <option value="train">train</option>
        <option value="test">test</option>
        <option value="single_prediction">single_prediction</option>
    </select>
    <br><br>
    <label for="image">Select File: </label>
    <input type="file" id="image" name="image" accept=".jpg, .jpeg, .png" multiple>
    <br><br>
    <label for="filename">File Name: </label>
    <input type="text" id="filename" name="filename">
    <br><br>
    <input type="submit" name="submit" value="Upload File">
</form>
{% endblock %}