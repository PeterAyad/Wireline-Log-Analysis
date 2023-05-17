import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_outliers(df_original, A, B):
    df_copy = df_original[[A, B]].copy()
    df_copy.dropna(inplace=True)
    # resistivity_to_log10(df_copy)
    # # select only the rows with outliers based on IQR
    non_outliers = df_copy[
        df_copy[B].between(
            df_copy[B].quantile(0.25), df_copy[B].quantile(0.75), inclusive=True
        )
    ]

    # plot the outliers
    plt.figure(figsize=(20, 10))
    sns.scatterplot(x=df_copy[A], y=df_copy[B], color="red")
    # mark the outliers on the plot
    sns.scatterplot(x=non_outliers[A], y=non_outliers[B], color="cornflowerblue")
    plt.title("Outliers in " + B + " vs " + A)
    plt.xlabel(A)
    plt.ylabel(B)
    plt.show()


def resistivity_to_log10(df):
    for col in df.columns:
        if "RES" in col.upper():
            df[col] = np.log10(df[col])


def rename_columns(df):
    df.rename(
        columns={
            "DEPTH_MD": "Measured Depth",
            "DEPT": "Measured Depth",
            "RDEP": "Deep Resistivity",
            "RSHA": "Shallow Resistivity",
            "RMED": "Medium Deep Resistivity",
            "RXO": "Flushed Zone Resistivity",
            "RMIC": "Micro Resistivity",
            "SP": "Self Potential",
            "DTS": "Shear wave sonic",
            "DTC": "Compressional waves sonic",
            "NPHI": "Neutron Porosity",
            "PEF": "Photo Electric Factor",
            "GR": "Gamma Ray",
            "RHOB": "Bulk Density",
            "DRHO": "Density Correction",
            "CALI": "Caliper",
            "BS": "Borehole Size",
            "DCAL": "Differential Caliper",
            "ROPA": "Average Rate of Penetration",
            "SGR": "Spectra Gamma Ray",
            "MUDWEIGHT": "Weight of Drilling Mud",
            "ROP": "Rate of Penetration",
            "URAN": "Uranium Concentration",
            "THOR": "Thorium Concentration",
            "RHOM": "Corrected Bulk Density",
            "DTE": "Sonic Slowness",
            "LITHOLOGY_GEOLINK": "LITHOLOGY",
            "FORCE_2020_LITHOFACIES_LITHOLOGY": "LITHOLOGY",
            "FORCE_2020_LITHOFACIES_CONFIDENCE": "CONFIDENCE",
        },
        inplace=True,
    )


def rename_lithology(df):
    df["LITHOLOGY"] = df["LITHOLOGY"].astype("str")
    df["LITHOLOGY"] = df["LITHOLOGY"].apply(lambda x: lithology_map[x])


def lithology_to_class(df):
    df["LITHOLOGY"] = df["LITHOLOGY"].apply(lambda x: lithology_to_class_number[x])


def class_to_lithology(df):
    df["LITHOLOGY"] = df["LITHOLOGY"].apply(lambda x: class_number_to_lithology[x])


class My_Columns:
    DEPTH = "Measured Depth"
    DEEP_RESISTIVITY = "Deep Resistivity"
    SHALLOW_RESISTIVITY = "Shallow Resistivity"
    MEDIUM_DEEP_RESISTIVITY = "Medium Deep Resistivity"
    FLUSHED_ZONE_RESISTIVITY = "Flushed Zone Resistivity"
    MICRO_RESISTIVITY = "Micro Resistivity"
    SELF_POTENTIAL = "Self Potential"
    SHEAR_WAVE_SONIC = "Shear wave sonic"
    COMPRESSIONAL_WAVES_SONIC = "Compressional waves sonic"
    NEUTRON_POROSITY = "Neutron Porosity"
    PHOTO_ELECTRIC_FACTOR = "Photo Electric Factor"
    GAMMA_RAY = "Gamma Ray"
    BULK_DENSITY = "Bulk Density"
    DENSITY_CORRECTION = "Density Correction"
    CALIPER = "Caliper"
    BOREHOLE_SIZE = "Borehole Size"
    DIFFERENTIAL_CALIPER = "Differential Caliper"
    AVERAGE_RATE_OF_PENETRATION = "Average Rate of Penetration"
    SPECTRA_GAMMA_RAY = "Spectra Gamma Ray"
    WEIGHT_OF_DRILLING_MUD = "Weight of Drilling Mud"
    RATE_OF_PENETRATION = "Rate of Penetration"
    LITHOLOGY = "LITHOLOGY"
    CONFIDENCE = "CONFIDENCE"
    FORMATION = "FORMATION"
    WELL = "WELL"
    GROUP = "GROUP"
    X_LOC = "X_LOC"
    Y_LOC = "Y_LOC"
    Z_LOC = "Z_LOC"
    FORMATION = "FORMATION"
    URANIUM = "Uranium Concentration"
    THORIUM = "Thorium Concentration"
    CORRECTED_BULK_DENSITY = "Corrected Bulk Density"
    SONIC_COMPRESSSIONAL_SLOWNESS = "Sonic Slowness"


lithology_map = {
    "35": "Sandstone",
    "22": "Anhydrite",
    "12": "Limestone",
    "36": "Sandstone",
    "23": "Basement",
    "25": "Shale",
    "16": "Limestone",
    "31": "Limestone",
    "14": "Shale",
    "33": "Halite",
    "9": "Chalk",
    "19": "Tuff",
    "18": "Coal",
    "17": "Shale",
    "3": "Sandstone",
    "15": "Dolomite",
    "26": "Shale",
    "21": "Halite",
    "34": "Halite",
    "11": "Limestone",
    "13": "Marl",
    "30": "Shale",
    "24": "Shale",
    "32": "Halite",
    "10": "Limestone",
    "1": "Sandstone",
    "4": "Shale",
    "8": "Shale",
    "6": "Shale",
    "5": "Shale",
    "2": "Sandstone",
    "7": "Shale",
    "29": "Shale",
    "27": "Shale",
    "28": "Shale",
    "20": "Tuff",
    "-999.250000": None,
    "30000": "Sandstone",
    "65030": "Sandstone/Shale",
    "65000": "Shale",
    "80000": "Marl",
    "74000": "Dolomite",
    "70000": "Limestone",
    "70032": "Chalk",
    "88000": "Halite",
    "86000": "Anhydrite",
    "99000": "Tuff",
    "90000": "Coal",
    "93000": "Basement",
    "35.0": "Sandstone",
    "22.0": "Anhydrite",
    "12.0": "Limestone",
    "36.0": "Sandstone",
    "23.0": "Basement",
    "25.0": "Shale",
    "16.0": "Limestone",
    "31.0": "Limestone",
    "14.0": "Shale",
    "33.0": "Halite",
    "9.0": "Chalk",
    "19.0": "Tuff",
    "18.0": "Coal",
    "17.0": "Shale",
    "3.0": "Sandstone",
    "15.0": "Dolomite",
    "26.0": "Shale",
    "21.0": "Halite",
    "34.0": "Halite",
    "11.0": "Limestone",
    "13.0": "Marl",
    "30.0": "Shale",
    "24.0": "Shale",
    "32.0": "Halite",
    "10.0": "Limestone",
    "1.0": "Sandstone",
    "4.0": "Shale",
    "8.0": "Shale",
    "6.0": "Shale",
    "5.0": "Shale",
    "2.0": "Sandstone",
    "7.0": "Shale",
    "29.0": "Shale",
    "27.0": "Shale",
    "28.0": "Shale",
    "20.0": "Tuff",
    "-999.25": None,
    "nan": None,
    "None": None,
    np.nan: None,
}

lithology_to_class_number = {
    "Sandstone": 0,
    "Anhydrite": 1,
    "Limestone": 2,
    "Basement": 3,
    "Shale": 4,
    "Halite": 5,
    "Chalk": 6,
    "Tuff": 7,
    "Coal": 8,
    "Dolomite": 9,
    "Marl": 10,
    "Sandstone/Shale": 11,
}

class_number_to_lithology = {
    0: "Sandstone",
    1: "Anhydrite",
    2: "Limestone",
    3: "Basement",
    4: "Shale",
    5: "Halite",
    6: "Chalk",
    7: "Tuff",
    8: "Coal",
    9: "Dolomite",
    10: "Marl",
    11: "Sandstone/Shale",
}

class_names = [
    "Sandstone",
    "Anhydrite",
    "Limestone",
    "Basement",
    "Shale",
    "Halite",
    "Chalk",
    "Tuff",
    "Coal",
    "Dolomite",
    "Marl",
    "Sandstone/Shale",
]
