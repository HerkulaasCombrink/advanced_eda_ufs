import os
import json
import tempfile
import streamlit as st
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="NetCDF Full Panel Exporter", layout="wide")

st.title("NetCDF Full Panel Exporter")
st.write(
    "Upload a NetCDF file to inspect its structure, plot variables, and export a fully "
    "flattened panel dataset including coordinates, all variables, and repeated metadata attributes."
)


def make_jsonable(value):
    """
    Convert attribute values into something safely serialisable for CSV export.
    """
    try:
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        if isinstance(value, (list, tuple, dict)):
            return json.dumps(value, default=str)
        return str(value)
    except Exception:
        return str(value)


def build_full_export_dataframe(ds: xr.Dataset) -> pd.DataFrame:
    """
    Convert the full xarray Dataset into a flat DataFrame that includes:
    - all coordinates
    - all data variables
    - dataset-level attributes repeated on every row
    - variable-level attributes repeated on every row

    This creates a deliberately repetitive panel-style table for downstream software.
    """
    # Flatten all coordinates + all variables
    df = ds.to_dataframe().reset_index()

    # Add dataset-level attributes to every row
    dataset_attrs = {
        f"dataset_attr_{key}": make_jsonable(value)
        for key, value in ds.attrs.items()
    }
    for col, val in dataset_attrs.items():
        df[col] = val

    # Add variable-level attributes to every row
    # These are repeated on every row because CSV is row-based
    for var_name in ds.data_vars:
        var_attrs = ds[var_name].attrs
        if var_attrs:
            for attr_key, attr_val in var_attrs.items():
                df[f"{var_name}_attr_{attr_key}"] = make_jsonable(attr_val)
        else:
            # Optional: keep an explicit marker showing variable had no attrs
            df[f"{var_name}_attr_info"] = "No attributes"

    # Add coordinate attributes as well
    for coord_name in ds.coords:
        coord_attrs = ds.coords[coord_name].attrs
        if coord_attrs:
            for attr_key, attr_val in coord_attrs.items():
                df[f"{coord_name}_coord_attr_{attr_key}"] = make_jsonable(attr_val)

    return df


uploaded_file = st.file_uploader("Upload a NetCDF file", type=["nc", "netcdf"])

if uploaded_file is not None:
    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".nc") as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_path = tmp_file.name

        ds = xr.open_dataset(temp_path)

        st.subheader("Dataset Overview")
        st.text(str(ds))

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Dimensions")
            st.write(dict(ds.sizes))

        with col2:
            st.subheader("Coordinates")
            st.write(list(ds.coords))

        st.subheader("Data Variables")
        data_vars = list(ds.data_vars)
        st.write(data_vars)

        st.subheader("Dataset Attributes")
        if ds.attrs:
            st.json({k: make_jsonable(v) for k, v in ds.attrs.items()})
        else:
            st.write("No dataset-level attributes found.")

        if data_vars:
            var_name = st.selectbox("Select a variable to inspect and plot", data_vars)
            da = ds[var_name]

            st.subheader("Selected Variable")
            st.text(str(da))

            st.subheader("Variable Attributes")
            if da.attrs:
                st.json({k: make_jsonable(v) for k, v in da.attrs.items()})
            else:
                st.write("No attributes found for this variable.")

            st.subheader("Plot")
            fig, ax = plt.subplots(figsize=(10, 6))

            # Plot logic for common dimensionalities
            if "time" in da.dims:
                time_index = st.slider(
                    "Select time index for plotting",
                    min_value=0,
                    max_value=max(0, da.sizes["time"] - 1),
                    value=0
                )

                sliced = da.isel(time=time_index)

                # If still multi-dimensional after slicing time, xarray will attempt a sensible plot
                sliced.plot(ax=ax)
            else:
                da.plot(ax=ax)

            st.pyplot(fig)

            st.subheader("Preview of Selected Variable as Table")
            try:
                if "time" in da.dims:
                    preview_df = da.isel(time=0).to_dataframe().reset_index()
                else:
                    preview_df = da.to_dataframe().reset_index()
                st.dataframe(preview_df.head(20))
            except Exception as e:
                st.warning(f"Could not create a variable preview table: {e}")

        st.subheader("Full Flattened Panel Export")
        st.write(
            "This export includes all coordinates, all variables, dataset attributes, "
            "variable attributes, and coordinate attributes. Metadata fields are repeated "
            "across rows so the file can be used in other software."
        )

        full_df = build_full_export_dataframe(ds)

        st.write("Full export shape:")
        st.write(full_df.shape)

        st.subheader("Preview of Full Export")
        st.dataframe(full_df.head(20))

        csv_data = full_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download full panel dataset with all variables and attributes",
            data=csv_data,
            file_name="full_panel_dataset_with_attributes.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"An error occurred while processing the NetCDF file: {e}")

    finally:
        if temp_path is not None and os.path.exists(temp_path):
            os.remove(temp_path)
