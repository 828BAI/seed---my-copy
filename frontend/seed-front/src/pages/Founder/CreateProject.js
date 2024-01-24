import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { resetRegistered, login } from "../../features/user";

function CreateProject() {
  const { user } = useSelector((state) => state.user);
  const email = user.user.email;

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("/api/project/manage", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      const data = await response.json();
      if (data.status === "success") {
        console.log("Project created successfully!");
      } else {
        console.log("Error:", data.message);
      }
    } catch (error) {
      console.log("Error:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email:
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </label>
      <button type="submit">Create Project</button>
    </form>
  );
}

export default CreateProject;
