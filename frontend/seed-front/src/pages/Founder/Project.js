import React, { useEffect } from "react";
import "./Project.css";
import Card from "../../components/Card";
import axios from "axios";
import { useSelector, useDispatch } from "react-redux";
import { getProject, reset } from "../../features/project";

const Project = () => {
  const { personalproject, isLoading, isSuccess, isError, message } =
    useSelector((state) => state.projectsList);
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getProject());
  }, [dispatch]);

  if (isLoading) {
    return (
      <div className="spinner-border" role="status">
        <span className="sr-only">Loading...</span>
      </div>
    );
  }

  if (isError) {
    return (
      <div className="right_content">
        <div className="title">
          <h1> My project</h1>
        </div>
        <div className="project_container">
          <div>Error: {message}</div>
        </div>
      </div>
    );
  } else if (isSuccess) {
    return (
      <div className="right_content">
        <div className="title">
          <h1> My project</h1>
        </div>
        <div className="project_container">
          <Card
            className="card-project"
            project_name={personalproject.project_name}
            description={personalproject.description}
            imageUrl={personalproject.project_image}
            investment={personalproject.investment}
            country={personalproject.country}
            end_date={personalproject.end_date}
            industry={personalproject.industry}
            slug={personalproject.slug}
          />
        </div>
      </div>
    );
  } else if (personalproject === null) {
    return (
      <div className="right_content">
        <div className="title">
          <h1> My project</h1>
        </div>
        <div className="project_container">
          <div className="noproject">
            <p> You haven't uploaded a project yet </p>
            <button> Add a project</button>
          </div>
        </div>
      </div>
    );
  }
};

export default Project;
