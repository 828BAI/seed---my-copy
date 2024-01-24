const express = require("express");
const cookieParser = require("cookie-parser");
const path = require("path");
require("dotenv").config();

const registerRoute = require("./routes/register");
const loginRoute = require("./routes/login");
const logoutRoute = require("./routes/logout");
const meRoute = require("./routes/me");
const verifyRoute = require("./routes/verify");
const displayprojectRoute = require("./routes/project/displayproject");
const createprojectRoute = require("./routes/project/createproject");
const detailView = require("./routes/project/detailview");

const app = express();
app.use(express.json());
app.use(cookieParser());

app.use(registerRoute);
app.use(loginRoute);
app.use(meRoute);
app.use(logoutRoute);
app.use(verifyRoute);
app.use(displayprojectRoute);
app.use(createprojectRoute);
app.use(detailView);
app.use(express.static("seed-front/build"));

app.get("*", (req, res) => {
  return res.sendFile(
    path.resolve(__dirname, "seed-front", "build", "index.html")
  );
});

const PORT = process.env.port || 4000;
app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));
