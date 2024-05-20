{% extends "base.html" %}

{% block head %} 
<title>Home Page</title>
{% endblock %}

{% block body %} 
<h1>Welcome to Home Page</h1>
<form method="POST" enctype="multipart/form-data">  
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

<?php 

if (isset($_POST['submit'])){
    $filename = $_POST['filename'];
    $image = $_FILES['image'];
    $chosenDirectory = $_POST['selectedOption'];

    $info = getimagesize($image['tmp_name']);

    if (!empty($info))
    {
        if ($image['type'] == "image/jpg" || $image['type'] == "image/jpeg" || $image['type'] == "image/png")
        {  
            if ($image['size'] <= 1024000)
            {
                //! Custom filename
                $ext = pathinfo($image['tmp_name'], PATHINFO_EXTENSION);
                $path = "models/covid19/$chosenDirectory/$filename.$ext";
                $check = move_uploaded_file($image['tmp_name'], $path);

                if ($check)
                {
                    echo "File uploaded successfully! <br>";

                    if ($image['type'] == "image/jpg" || $image['type'] == "image/jpeg")
                    {
                        $source = imagecreatefromjpeg($path);
                    } 
                    
                    else 
                    {
                        $source = imagecreatefrompng($path);
                    }

                    $width = imagesx($source);
                    $height = imagesy($source);
                } 
                
                else 
                {
                    echo "File upload failed! . <br>";
                }
            } 
            
            else 
            {
                echo "File size is too large! . <br>";
            }    
        } 
        
        else 
        {
            echo "File type is not supported! . <br>";
        }
    }

    else
    {
        echo "File is not an image! . <br>";
    }
}

?>
