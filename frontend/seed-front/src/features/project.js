import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

export const getProject = createAsyncThunk(
  "project/show",
  async (_, thunkAPI) => {
    try {
      const res = await fetch("/api/project/show", {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      });

      const data = await res.json();

      if (res.status === 200) {
        return data;
      } else {
        return thunkAPI.rejectWithValue(data);
      }
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data);
    }
  }
);

export const createProject = createAsyncThunk(
  "project/create",
  async (
    {
      project_name,
      webiste,
      country,
      description,
      investment,
      stage,
      industry,
      project_image,
      presentation,
      video,
      papers,
    },
    thunkAPI
  ) => {
    const body = JSON.stringify({
      project_name,
      webiste,
      country,
      description,
      investment,
      stage,
      industry,
      project_image,
      presentation,
      video,
      papers,
    });

    try {
      const res = await fetch("/api/project/create", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body,
      });

      const data = await res.json();

      if (res.status === 200) {
        return data;
      } else {
        return thunkAPI.rejectWithValue(data);
      }
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data);
    }
  }
);

export const updateProject = createAsyncThunk(
  "/project/update",
  async (
    {
      project_name,
      webiste,
      country,
      description,
      investment,
      stage,
      industry,
      project_image,
      presentation,
      video,
      papers,
    },
    thunkAPI
  ) => {
    const body = JSON.stringify({
      project_name,
      webiste,
      country,
      description,
      investment,
      stage,
      industry,
      project_image,
      presentation,
      video,
      papers,
    });

    try {
      const res = await fetch("/api/project/create", {
        method: "PUT",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body,
      });

      const data = await res.json();

      if (res.status === 200) {
        return data;
      } else {
        return thunkAPI.rejectWithValue(data);
      }
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data);
    }
  }
);

export const getProjectDetail = createAsyncThunk(
  `project/:detail`,
  async (_, thunkAPI) => {
    try {
      const res = await fetch(`/api/project/:${slug}`, {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      });

      const data = await res.json();

      if (res.status === 200) {
        return data;
      } else {
        return thunkAPI.rejectWithValue(data);
      }
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data);
    }
  }
);

const initialState = {
  allprojects: [],
  personalproject: null,
  isError: false,
  isLoading: false,
  isSuccess: false,
  message: "",
};

export const projectSlice = createSlice({
  name: "projectsList",
  initialState,
  reducers: {
    reset: (state) => initialState,
  },
  extraReducers: (builders) => {
    builders
      .addCase(getProject.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getProject.fulfilled, (state, action) => {
        state.isLoading = false;
        state.isSuccess = true;
        state.personalproject = action.payload;
      })
      .addCase(getProject.rejected, (state, action) => {
        state.isLoading = false;
        state.isError = true;
        state.message = action.payload;
      })
      .addCase(getProjectDetail.pending, (state) => {
        state.isLoading = true;
      })
      .addCase(getProjectDetail.fulfilled, (state, action) => {
        state.isLoading = false;
        state.isSuccess = true;
        state.personalproject = action.payload;
      })
      .addCase(getProjectDetail.rejected, (state, action) => {
        state.isLoading = false;
        state.isError = true;
        state.message = action.payload;
      });
  },
});

export const { reset } = projectSlice.actions;
export default projectSlice.reducer;
