<!DOCTYPE html>
<html><body>
<h1>Monitoreo de BMP180</h1>
<?php

$servername = "localhost";
$dbname = "id19071410_monitoreo";
$username = "id19071410_bpaz";
$password = "Inictel.2022";

// Creando Conexion
$conn = new mysqli($servername, $username, $password, $dbname);
// Verificando conexion
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT id, sensor, location, value1, value2, value3, reading_time FROM SensorData ORDER BY id DESC";

echo '<table cellspacing="5" cellpadding="5">
      <tr> 
        <td>ID</td> 
        <td>Sensor</td> 
        <td>Localizacion</td> 
        <td>Temperatura</td> 
        <td>Altitud</td>
        <td>Presion</td> 
        <td>Fecha y Hora</td> 
      </tr>';
 
if ($result = $conn->query($sql)) {
    while ($row = $result->fetch_assoc()) {
        $row_id = $row["id"];
        $row_sensor = $row["sensor"];
        $row_location = $row["location"];
        $row_value1 = $row["value1"];
        $row_value2 = $row["value2"]; 
        $row_value3 = $row["value3"]; 
        $row_reading_time = $row["reading_time"];
        // Si se desea calibrar a la hora, descomentar
        //$row_reading_time = date("Y-m-d H:i:s", strtotime("$row_reading_time + 4 hours"));
      
        echo '<tr> 
                <td>' . $row_id . '</td> 
                <td>' . $row_sensor . '</td> 
                <td>' . $row_location . '</td> 
                <td>' . $row_value1 . '</td> 
                <td>' . $row_value2 . '</td>
                <td>' . $row_value3 . '</td> 
                <td>' . $row_reading_time . '</td> 
              </tr>';
    }
    $result->free();
}

$conn->close();
?> 
</table>
</body>
</html>