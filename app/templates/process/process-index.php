<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>
</head>
<body>
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
                $path = "../models/covid19/$chosenDirectory/$filename.$ext";
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
</body>
</html>