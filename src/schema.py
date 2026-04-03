from pydantic import BaseModel, Field


class ForecastInput(BaseModel):
    month_index: int = Field(..., ge=0, description="Index temporel du mois")
    tla_tldds: float = Field(..., ge=0, description="Taux Livret A / LDDS")
    tlep: float = Field(..., ge=0, description="Taux LEP")


class ForecastResponse(BaseModel):
    predicted_flux_la_ldds: float
