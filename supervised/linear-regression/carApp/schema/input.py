from pydantic import BaseModel, Field
from typing import Annotated, Optional
from datetime import datetime


currYear = datetime.now().year

# 0 > year
# 1 > mileage
# 2 > tax
# 3 > mpg
# 4 > engineSize
# 5 > model_ C-MAX
# 6 > model_ EcoSport
# 7 > model_ Edge
# 8 > model_ Escort
# 9 > model_ Fiesta
# 10 > model_ Focus
# 11 > model_ Fusion
# 12 > model_ Galaxy
# 13 > model_ Grand C-MAX
# 14 > model_ Grand Tourneo Connect
# 15 > model_ KA
# 16 > model_ Ka+
# 17 > model_ Kuga
# 18 > model_ Mondeo
# 19 > model_ Mustang
# 20 > model_ Puma
# 21 > model_ Ranger
# 22 > model_ S-MAX
# 23 > model_ Streetka
# 24 > model_ Tourneo Connect
# 25 > model_ Tourneo Custom
# 26 > model_ Transit Tourneo
# 27 > model_Focus
# 28 > transmission_Manual
# 29 > transmission_Semi-Auto
# 30 > fuelType_Electric
# 31 > fuelType_Hybrid
# 32 > fuelType_Other
# 33 > fuelType_Petrol

from pydantic import BaseModel, Field
from typing import Annotated, Literal
from datetime import datetime

currYear = datetime.now().year


class Input(BaseModel):

    # Numerical features
    year: Annotated[
        int,
        Field(..., gt=1900, le=currYear, description="Year of manufacture"),
    ]

    mileage: Annotated[
        int,
        Field(..., ge=0, description="Mileage of the car"),
    ]

    tax: Annotated[
        int,
        Field(..., ge=0, description="Road tax"),
    ]

    mpg: Annotated[
        float,
        Field(..., gt=0, description="Miles per gallon"),
    ]

    engineSize: Annotated[
        float,
        Field(..., gt=0, description="Engine size in liters"),
    ]

    # Categorical features (VERY IMPORTANT)
    model: Annotated[
        Literal[
            "C-MAX",
            "EcoSport",
            "Edge",
            "Escort",
            "Fiesta",
            "Focus",
            "Fusion",
            "Galaxy",
            "Grand C-MAX",
            "Grand Tourneo Connect",
            "KA",
            "Ka+",
            "Kuga",
            "Mondeo",
            "Mustang",
            "Puma",
            "Ranger",
            "S-MAX",
            "Streetka",
            "Tourneo Connect",
            "Tourneo Custom",
            "Transit Tourneo",
        ],
        Field(
            ...,
            title="Model",
            description="Model of the car",
        ),
    ]

    transmission: Annotated[
        Literal["Manual", "Semi-Auto"],
        Field(
            ...,
            title="Transmission",
            description="Transmission type of the car",
        ),
    ]

    fuelType: Annotated[
        Literal["Petrol", "Diesel", "Hybrid", "Electric", "Other"],
        Field(
            ...,
            title="Fuel Type",
            description="Fuel type of the car",
        ),
    ]


