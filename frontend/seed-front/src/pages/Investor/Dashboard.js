import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import checkAuth from "../../features/user";
import Sidebar_inv from "../../components/Sidebar_inv";
import "./Dashboard.css";

const Dashboard = () => {
  return (
    <div className="Dashboard">
      <Sidebar_inv className="Side" />
    </div>
  );
};

export default Dashboard;
