import streamlit as st
import plotly.express as px
from backend import get_data
# add header ,place , selectbox
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the Temperature and Sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
        # create a temperature plot
            figure = px.line(x=dates, y=temperature, labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "image/clear.png", "Clouds": "image/cloud.png",
                      "Rain": "image/rain.png", "Snow": "image/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path = [images[condition] for condition in sky_condition ]
            st.image(image_path, width=115)
    except KeyError:
        st.write("That place doesn't exit.")