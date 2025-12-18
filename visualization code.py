import pandas as pd
import matplotlib.pyplot as plt


# Load cleaned dataset
# =========================
df = pd.read_csv("cleaned_disaster_dataset.csv")

# Convert event_time to datetime (handles mixed formats)
df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")

# =========================
# 1. Disaster Count by Type
# =========================
plt.figure()
df["event_type"].value_counts().plot(kind="bar")
plt.title("Disaster Count by Type")
plt.xlabel("Disaster Type")
plt.ylabel("Number of Events")
plt.show()

# =========================
# 2. Severity Distribution
# =========================
plt.figure()
plt.hist(df["severity"], bins=20)
plt.title("Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Frequency")
plt.show()

# =========================
# 3. Disaster Events Over Time
# =========================
plt.figure()
df.dropna(subset=["event_time"]) \
  .set_index("event_time") \
  .resample("h") \
  .size() \
  .plot()

plt.title("Disaster Events Over Time (Hourly)")
plt.xlabel("Time")
plt.ylabel("Number of Events")
plt.show()

# =========================
# 4. Geographic Distribution
# =========================
plt.figure()
plt.scatter(df["longitude"], df["latitude"], alpha=0.5)
plt.title("Geographic Distribution of Disasters")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# =========================
# 5. Average Severity by Disaster Type
# =========================
plt.figure()
df.groupby("event_type")["severity"].mean().plot(kind="bar")
plt.title("Average Severity by Disaster Type")
plt.xlabel("Disaster Type")
plt.ylabel("Average Severity")
plt.show()