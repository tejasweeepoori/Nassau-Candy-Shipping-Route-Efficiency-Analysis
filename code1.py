# ==========================================
# Nassau Candy Shipping Route Analysis
# ==========================================

# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("Nassau Candy Distributor.csv")

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())


# ==========================================
# 2. DATA INFORMATION
# ==========================================

print("\nDataset Information:")
print(df.info())


print("\nMissing Values:")
print(df.isnull().sum())


# Remove duplicates

df.drop_duplicates(inplace=True)

print("\nShape after removing duplicates:", df.shape)



# ==========================================
# 3. DATE CLEANING
# ==========================================

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    dayfirst=True
)

# ==========================================
# 4. FEATURE ENGINEERING
# ==========================================

# Shipping Lead Time

df["Lead_Time"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days


# Remove invalid values

df = df[df["Lead_Time"] >= 0]


print("\nLead Time Created")
print(df[["Order Date","Ship Date","Lead_Time"]].head())



# ==========================================
# 5. FACTORY INFORMATION
# ==========================================

factory_coordinates = {

    "Lot's O' Nuts":
    (32.881893,-111.768036),

    "Wicked Choccy's":
    (32.076176,-81.088371),

    "Sugar Shack":
    (48.11914,-96.18115),

    "Secret Factory":
    (41.446333,-90.565487),

    "The Other Factory":
    (35.1175,-89.971107)

}



# ==========================================
# 6. PRODUCT - FACTORY MAPPING
# ==========================================


factory_mapping = {


"Wonka Bar - Nutty Crunch Surprise":
"Lot's O' Nuts",

"Wonka Bar - Fudge Mallows":
"Lot's O' Nuts",

"Wonka Bar -Scrumdiddlyumptious":
"Lot's O' Nuts",

"Wonka Bar - Milk Chocolate":
"Wicked Choccy's",

"Wonka Bar - Triple Dazzle Caramel":
"Wicked Choccy's",


"Laffy Taffy":
"Sugar Shack",

"SweeTARTS":
"Sugar Shack",

"Nerds":
"Sugar Shack",

"Fun Dip":
"Sugar Shack",

"Fizzy Lifting Drinks":
"Sugar Shack",


"Everlasting Gobstopper":
"Secret Factory",

"Hair Toffee":
"The Other Factory",

"Lickable Wallpaper":
"Secret Factory",

"Wonka Gum":
"Secret Factory",

"Kazookles":
"The Other Factory"

}



# Create Factory Column

df["Factory"] = df["Product Name"].map(factory_mapping)


print("\nFactory Assignment:")
print(df[["Product Name","Factory"]].head())



# ==========================================
# 7. ROUTE CREATION
# ==========================================


df["Route"] = (

    df["Factory"]
    +
    " → "
    +
    df["State/Province"]

)



print("\nRoutes:")
print(df["Route"].head())



# ==========================================
# 8. KPI CALCULATIONS
# ==========================================


total_orders = df["Order ID"].nunique()

average_lead_time = df["Lead_Time"].mean()

total_sales = df["Sales"].sum()

total_profit = df["Gross Profit"].sum()



print("\n========== KPIs ==========")

print("Total Orders:", total_orders)

print("Average Lead Time:",
      round(average_lead_time,2),
      "days")

print("Total Sales:",
      round(total_sales,2))

print("Total Profit:",
      round(total_profit,2))



# ==========================================
# 9. ROUTE ANALYSIS
# ==========================================


route_analysis = (

df.groupby("Route")
.agg(

Total_Shipments=("Order ID","count"),

Average_Lead_Time=("Lead_Time","mean"),

Total_Sales=("Sales","sum"),

Average_Profit=("Gross Profit","mean")

)

.reset_index()

)



print("\nRoute Analysis")

print(route_analysis.head())



# ==========================================
# 10. BEST ROUTES
# ==========================================


best_routes = (

route_analysis
.sort_values(
"Average_Lead_Time"
)
.head(10)

)


print("\nTOP 10 EFFICIENT ROUTES")

print(best_routes)



# ==========================================
# 11. WORST ROUTES
# ==========================================


worst_routes = (

route_analysis
.sort_values(
"Average_Lead_Time",
ascending=False
)
.head(10)

)


print("\nWORST 10 ROUTES")

print(worst_routes)



# ==========================================
# 12. DELAY ANALYSIS
# ==========================================


df["Shipment_Status"] = np.where(

df["Lead_Time"] > 5,

"Delayed",

"On Time"

)



delay_percentage = (

df["Shipment_Status"]
.value_counts(normalize=True)
*100

)



print("\nDelay Percentage")

print(delay_percentage)



# ==========================================
# 13. SHIP MODE ANALYSIS
# ==========================================


ship_mode_analysis = (

df.groupby("Ship Mode")
["Lead_Time"]
.mean()
.sort_values()

)



print("\nShip Mode Performance")

print(ship_mode_analysis)



# ==========================================
# 14. VISUALIZATIONS
# ==========================================


# Lead Time Distribution

plt.figure(figsize=(8,5))

sns.histplot(

df["Lead_Time"],

bins=20,

kde=True

)

plt.title(
"Shipping Lead Time Distribution"
)

plt.xlabel(
"Days"
)

plt.show()



# Best Routes Chart


plt.figure(figsize=(10,6))


sns.barplot(

data=best_routes,

x="Average_Lead_Time",

y="Route"

)


plt.title(
"Top Efficient Routes"
)

plt.show()



# Ship Mode Chart


plt.figure(figsize=(8,5))


sns.barplot(

x=ship_mode_analysis.index,

y=ship_mode_analysis.values

)


plt.xticks(rotation=45)

plt.ylabel(
"Average Lead Time"
)


plt.title(
"Ship Mode Efficiency"
)


plt.show()



# ==========================================
# 15. SAVE FINAL DATA
# ==========================================


df.to_csv(
"clean_shipping_data.csv",
index=False
)


route_analysis.to_csv(
"route_analysis.csv",
index=False
)


print("\nFiles Saved Successfully!")
print("clean_shipping_data.csv")
print("route_analysis.csv")