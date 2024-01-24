import React from "react";
import "./ProjectDetailView.css";
import { useParams, useNavigate, useLocation } from "react-router-dom";
import { getProject, reset } from "../features/project";
import { useSelector, useDispatch } from "react-redux";

const displayTags = (tags) => {
  return tags.map((tag) => {
    return <Tags>{tag}</Tags>;
  });
};

const ProjectDetailView = () => {
  const { slug } = useParams();

  const { personalproject, isLoading, isSuccess, isError, message } =
    useSelector((state) => state.projectsList);
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getProjectDetail());
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
      <div className="alert alert-danger" role="alert">
        {message}
      </div>
    );
  }
  if (isSuccess) {
    console.log("hi!");
    return (
      <div className="project-content">
        <div className="project-content__header">
          <h1 className="project-content__title">
            {personalproject.project_name}
          </h1>
          <p className="project-content__description">
            {personalproject.description}
          </p>
        </div>
        <div className="project-content__body">
          {displayTags(industry)}
          <img src={personalproject.project_image} alt="" />
        </div>
        <div className="project-content__left">
          <div className="project-content__investment">
            <h2> {personalproject.investment} in demand</h2>
          </div>
          <div className="project-content__country">
            <h2> {personalproject.country}</h2>
          </div>
          <div className="project-content__end-date">
            <h2> {personalproject.end_date} days left</h2>
          </div>
        </div>
      </div>
    );
  }
};

export default ProjectDetailView;
