import "./Dashboard_founder.css";
import Sidebar_founder from "../../components/Sidebar_founder";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Project from "./Project";
import { useSelector } from "react-redux";
import React, { useEffect } from "react";
import { useDispatch } from "react-redux";
import checkAuth from "../../features/user";

const Dashboard = () => {
  return (
    <div className="Dashboard">
      <Sidebar_founder className="Side-found" />
    </div>
  );
};

export default Dashboard;
