from geopy.geocoders import Nominatim
import plotly.graph_objects as go

def find_lat_long(adress=str):
    geolocator = Nominatim(user_agent="my_user_agent")
    location = geolocator.geocode(adress)
    print("latitude is :-" ,location.latitude,"\nlongtitude is:-" ,location.longitude)
    return location.latitude, location.longitude


def plot_lat_long(latitude, longitude):
    mapbox_access_token = open(".mapbox_token").read()

    fig = go.Figure(go.Scattermapbox(
            lat=[str(latitude)],
            lon=[str(longitude)],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=14
            ),
            text=['Montreal'],
        ))

    fig.update_layout(
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=45,
                lon=-73
            ),
            pitch=0,
            zoom=5
        )
    )

    fig.show()

def gmplot_test():
    from gmplot import gmplot

    # Initialize the map at a given point
    gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13)

    # Add a marker
    gmap.marker(37.770776, -122.461689, 'cornflowerblue')

    # Draw map into HTML file
    gmap.draw("my_map.html")




# lat, long = find_lat_long('Florianopolis, Brazil')
# plot_lat_long(lat, long)
gmplot_test()