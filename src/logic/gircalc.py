"""
zr = zini + max((zmax-zini)*min(1, (doy-ldev-plant)/(lmid-ldev)), 0) ???
zr = IF(A4 <= AE4, AC4, AC4 + (AD4 - AC4) * POWER((A4 - AE4/2) / (AF4- AE4/2), 1/AG4))
taw = aw * zr
raw = taw * mad
eta (input)
precipitation (input)
di = acc(eta - precipitation)
lr = ecw/(5*ece-ecw)
r (input: bool) (unrelated)
f # number of skipped days
dg = mad - di (first time)
dg = IF(lr > 0.1, di / 0.55 * (1 - lr), di / 0.55)
gir = dg * a * 4200 / 1000
"""

from typing import NamedTuple


class Params(NamedTuple):
    """The interface between the UI and the functions. Carries all params required by all functions."""

    # global
    area: float
    aw: float
    ece: float
    ecw: float
    mad: float
    zn: float
    zo: float
    zx: float
    to: int
    tx: int
    n: float

    # local
    doy: int
    eta: float
    precipitation: float

    @property
    def zr(self) -> float:
        if self.doy < self.to:
            return self.zo

        return self.zo + (self.zx - self.zo) * (
            (self.doy - self.to / 2) / (self.tx - self.to / 2)
        ) ** (1 / self.n)

    @property
    def taw(self) -> float:
        return self.aw * self.zr

    @property
    def raw(self) -> float:
        return self.taw * self.mad

    @property
    def di(self) -> float:
        return self.eta - self.precipitation

    @property
    def lr(self) -> float:
        return self.ecw / (5 * self.ece - self.ecw)

    @property
    def gir(self) -> float:
        di = self.di
        if self.lr > 0.1:
            dg = di / 0.55 * (1 - self.lr)
        else:
            dg = di / 0.55
        return dg * self.area * 4200 / 1000


if __name__ == "__main__":
    pass
