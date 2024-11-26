const axios = require("axios");

// Function to handle prediction logic
exports.predictWeather = async (req, res) => {
  const { temperature, humidity, windSpeed, city, day, hour } = req.body;

  try {
    // Call Flask API
    const response = await axios.post("http://localhost:5000/predict", {
      temperature,
      humidity,
      windSpeed,
      city,
      day,
      hour,
    });

    res.json(response.data); // Send the prediction back to the frontend
  } catch (error) {
    console.error("Error calling Flask API:", error.message);
    res.status(500).send({
      error: "Error calling prediction service",
      details: error.message,
    });
  }
};
