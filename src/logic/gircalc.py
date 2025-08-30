from typing import NamedTuple


class Params(NamedTuple):
    """
    Container for parameters and derived irrigation calculations.

    Fields are grouped into:
      - global parameters (area, aw, ece, ecw, mad, zo, zx, to, tx, n)
      - local parameters (doy, eta, precipitation)
    """

    # global
    area: float
    aw: float
    ece: float
    ecw: float
    mad: float
    zo: float  # initial rooting depth
    zx: float  # maximum rooting depth
    to: int    # development start DOY
    tx: int    # development end DOY
    n: float   # curve shape parameter

    # local
    doy: int             # current day of year
    eta: float           # evapotranspiration [mm/day]
    precipitation: float # precipitation [mm/day]

    # --- Derived values ---

    @property
    def zr(self) -> float:
        """Root depth [m] at current DOY."""
        if self.doy < self.to:
            return self.zo
        return self.zo + (self.zx - self.zo) * (
            (self.doy - self.to) / (self.tx - self.to)
        ) ** (1 / self.n)

    @property
    def taw(self) -> float:
        """Total available water [mm]."""
        return self.aw * self.zr

    @property
    def raw(self) -> float:
        """Readily available water [mm]."""
        return self.taw * self.mad

    @property
    def di(self) -> float:
        """Daily net irrigation requirement [mm]."""
        return self.eta - self.precipitation

    @property
    def lr(self) -> float:
        """Leaching requirement (dimensionless)."""
        return self.ecw / (5 * self.ece - self.ecw)

    def dg(self, first_time: bool = False) -> float:
        """
        Gross irrigation depth [mm].
        If first_time is True, special initialization branch is applied.
        """
        if first_time:
            return self.mad - self.di
        if self.lr > 0.1:
            return self.di / 0.55 * (1 - self.lr)
        return self.di / 0.55

    def gir(self, first_time: bool = False) -> float:
        """
        Gross irrigation requirement [m³].
        Converts depth (dg) to volume using area and water density.
        """
        return self.dg(first_time) * self.area * 4200 / 1000



if __name__ == "__main__":
    params = Params(
        area=1.5,
        aw=100,
        ece=3,
        ecw=0.5,
        mad=0.6,
        zo=0.3,
        zx=1.2,
        to=120,
        tx=200,
        n=2,
        doy=150,
        eta=5,
        precipitation=2,
    )

    print("zr =", params.zr)
    print("taw =", params.taw)
    print("raw =", params.raw)
    print("di =", params.di)
    print("lr =", params.lr)
    print("dg =", params.dg())
    print("gir =", params.gir())

