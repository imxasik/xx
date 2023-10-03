import numpy as np
import ftplib
import io
import matplotlib.pyplot as plt

# Generate random data for time, latitude, and the parameter of interest (e.g., temperature).
num_time_steps = 100
num_latitudes = 50

# Generate random time values (e.g., years).
time_values = np.linspace(2000, 2020, num_time_steps)

# Generate random latitude values (e.g., degrees north).
latitude_values = np.linspace(-90, 90, num_latitudes)

# Generate random temperature values (replace with your parameter of interest).
temperature_data = np.random.rand(num_latitudes, num_time_steps) * 30 - 10  # Random values between -10°C and 20°C.

# Create a Hovmoller-like plot.
plt.figure(figsize=(10, 6))
plt.pcolormesh(time_values, latitude_values, temperature_data, cmap='viridis', shading='auto')
plt.colorbar(label='Temperature (°C)')
plt.title('Random Hovmoller-Like Diagram')
plt.xlabel('Time')
plt.ylabel('Latitude (°N)')
plt.gca().invert_yaxis()  # Reverse the y-axis to have the North Pole at the top.
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot to a BytesIO buffer
plot_buffer = io.BytesIO()
plt.savefig(plot_buffer, format="jpg", transparent=True)
plot_buffer.seek(0)

# FTP Server Details
ftp_host = "ftpupload.net"
ftp_username = "epiz_32144154"
ftp_password = "Im80K123"

# Connect to the FTP server and upload the plot directly
with ftplib.FTP(ftp_host) as ftp:
    ftp.login(ftp_username, ftp_password)
    ftp.cwd('htdocs/wx')  # Change directory to your desired location on the FTP server
    ftp.storbinary('STOR hov.jpg', plot_buffer)

plt.show()
