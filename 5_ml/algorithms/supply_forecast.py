"""
Material Supply / Demand Forecasting
------------------------------------
Forecasts near-future raw-material availability or demand from
historical time-series data, to anticipate shortages before they
interrupt production.

Uses Holt-Winters Exponential Smoothing: lightweight, works well on
relatively short pharma supply-chain series, and natively captures
trend + seasonality (e.g. periodic demand cycles) without requiring
a large training dataset like deep-learning forecasters would.
"""

import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing


class SupplyForecastModel:
    def __init__(self, seasonal_periods: int = 12):
        self.seasonal_periods = seasonal_periods
        self.model = None
        self.fitted = None

    def fit(self, series: np.ndarray):
        """series: chronologically ordered historical values (e.g. monthly)."""
        self.model = ExponentialSmoothing(
            series,
            trend="add",
            seasonal="add",
            seasonal_periods=self.seasonal_periods,
        )
        self.fitted = self.model.fit()

    def forecast(self, periods_ahead: int = 3) -> np.ndarray:
        """Forecast the next `periods_ahead` points (e.g. next 3 months)."""
        if self.fitted is None:
            raise RuntimeError("Model must be fit before forecasting.")
        return self.fitted.forecast(periods_ahead)
