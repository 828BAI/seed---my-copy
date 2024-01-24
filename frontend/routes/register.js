const express = require("express");
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));

const router = express.Router();

router.post("/api/users/register", async (req, res) => {
  const { name, last_name, email, password, re_password, is_founder } =
    req.body;

  const body = JSON.stringify({
    name,
    last_name,
    email,
    password,
    re_password,
    is_founder,
  });
  try {
    const registerRes = await fetch(
      `${process.env.API_URL}/api/users/register`,
      {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body,
      }
    );
    const data = await registerRes.json();
    console.log(data);
    return res.status(registerRes.status).json();
  } catch (err) {
    return res.status(500).json({
      error: "Something went wrong when registering account",
    });
  }
});
module.exports = router;
