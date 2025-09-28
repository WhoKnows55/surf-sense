# app/app.py
import os
import streamlit as st
import requests
from datetime import datetime, timezone

STORMGLASS_KEY = os.getenv("STORMGLASS_KEY")

def get_surf_point(lat, lng, params="waveHeight,swellHeight,swellDirection,windSpeed"):
    url = "https://api.stormglass.io/v2/weather/point"
    headers = {"Authorization": STORMGLASS_KEY}
    
    # Add required start/end timestamps
    now = datetime.now(timezone.utc)
    start = now.isoformat()
    end = (now.replace(hour=23, minute=59, second=59)).isoformat()
    
    params_q = {
        "lat": lat, 
        "lng": lng, 
        "params": params,
        "start": start,
        "end": end
    }
    
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
            st.json(data)
        except Exception as e:
            st.error(f"Error fetching data: {e}")