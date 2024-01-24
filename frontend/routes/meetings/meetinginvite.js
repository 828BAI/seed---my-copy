const express = require("express");
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));

const router = express.Router();

router.post("/api/create_meeting/<slug:slug>", async (req, res) => {
  const { option_1_time, option_2_time, option_3_time } = req.body;

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
