import streamlit as st
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
import tempfile


st.set_page_config(page_title="NetCDF Viewer", layout="wide")

st.title("NetCDF File Viewer")
st.write(
    "Upload a NetCDF file, inspect its structure, preview variables, "
    "plot the data, and view a tabular sample."
)

uploaded_file = st.file_uploader("Upload a NetCDF file", type=["nc", "netcdf"])

if uploaded_file is not None:
    try:
        # Save uploaded file temporarily so xarray can open it
        with tempfile.NamedTemporaryFile(delete=False, suffix=".nc") as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_path = tmp_file.name

        ds = xr.open_dataset(temp_path)

        st.subheader("Dataset Overview")
        st.text(str(ds))

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Dimensions")
            st.write(dict(ds.dims))

        with col2:
            st.subheader("Coordinates")
            st.write(list(ds.coords))

        st.subheader("Data Variables")
        data_vars = list(ds.data_vars)
        st.write(data_vars)

        if not data_vars:
            st.warning("No data variables were found in this dataset.")
        else:
            var_name = st.selectbox("Select a variable to inspect", data_vars)
            da = ds[var_name]

            st.subheader("Selected Variable")
            st.text(str(da))

            st.subheader("Variable Attributes")
            st.write(dict(da.attrs) if da.attrs else "No attributes found.")

            st.subheader("Plot")

            fig, ax = plt.subplots(figsize=(10, 6))

            if "time" in da.dims:
                time_index = st.slider(
                    "Select time index",
                    min_value=0,
                    max_value=max(0, da.sizes["time"] - 1),
                    value=0
                )
                da.isel(time=time_index).plot(ax=ax)
            else:
                da.plot(ax=ax)

            st.pyplot(fig)

            st.subheader("Data Preview")

            if "time" in da.dims:
                df = da.isel(time=0).to_dataframe().reset_index()
            else:
                df = da.to_dataframe().reset_index()

            st.dataframe(df.head())

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download preview data as CSV",
                data=csv,
                file_name=f"{var_name}_preview.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
