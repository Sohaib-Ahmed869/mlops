const cookieParser = require("cookie-parser");
const express = require("express");
const dotenv = require("dotenv");
const app = express();

app.use(cookieParser());
app.use(express.json());

const WeatherRoutes = require("./Routes/weatherRoutes");

app.use("/weather", WeatherRoutes);

const PORT = process.env.PORT || 3001;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
