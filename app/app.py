# app/app.py
import os
import streamlit as st
import requests

STORMGLASS_KEY = os.getenv("STORMGLASS_KEY")  # set in .env locally, GitHub Secrets for CI

def get_surf_point(lat, lng, params="waveHeight,swells,swellDirection,windSpeed"):
    url = "https://api.stormglass.io/v2/weather/point"
    headers = {"Authorization": STORMGLASS_KEY}
    params_q = {"lat": lat, "lng": lng, "params": params}
    resp = requests.get(url, headers=headers, params=params_q, timeout=10)
    resp.raise_for_status()
    return resp.json()

st.title("SurfSense — surf trip assistant (MVP)")

lat = st.number_input("Latitude", value=38.7071, format="%.6f")
lng = st.number_input("Longitude", value=-9.1360, format="%.6f")
if st.button("Fetch surf forecast"):
    if not STORMGLASS_KEY:
        st.error("No STORMGLASS_KEY set in environment.")
    else:
        try:
            data = get_surf_point(lat, lng)
            st.json(data)  # iterate and show summary in tabular form next
        except Exception as e:
            st.error(f"Error fetching data: {e}")
