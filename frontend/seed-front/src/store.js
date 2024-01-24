import userReducer from "../src/features/user";
import { configureStore } from "@reduxjs/toolkit";
import projectReducer from "../src/features/project";

export const store = configureStore({
  reducer: {
    user: userReducer,
    projectsList: projectReducer,
  },
  devTools: process.env.NODE_ENV !== "production",
});
