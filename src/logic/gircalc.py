from itertools import takewhile
from typing import NamedTuple


class GlobalParams(NamedTuple):
    area: float
    aw: float
    ece: float
    ecw: float
    mad: float
    zo: float
    zx: float
    to: int
    tx: int
    n: float


class LocalParams(NamedTuple):
    g: GlobalParams
    doy: int
    eta: float
    precipitation: float
    r: bool = False
    previous: "LocalParams | None" = None

    @property
    def zr(self) -> float:
        g = self.g
        if self.doy < g.to:
            return g.zo
        return g.zo + (g.zx - g.zo) * ((self.doy - g.to / 2) / (g.tx - g.to / 2)) ** (
            1 / g.n
        )

    @property
    def taw(self) -> float:
        return self.g.aw * self.zr

    @property
    def raw(self) -> float:
        return self.taw * self.g.mad

    @property
    def di(self) -> float:
        base = self.eta - self.precipitation
        if self.previous is None:
            return base
        return base + self.previous.di

    @property
    def lr(self) -> float:
        g = self.g
        return g.ecw / (5 * g.ece - g.ecw)

    @property
    def dg(self) -> float:
        g, di = self.g, self.di
        if self.previous is None:
            return g.mad - di
        if self.lr > 0.1:
            return di / 0.55 * (1 - self.lr)
        return di / 0.55

    @property
    def gir(self) -> float:
        return self.dg * self.g.area * 4200 / 1000

    @property
    def f(self) -> int:
        if not self.r:
            return 0
        skipped = takewhile(lambda lp: not lp.r, self._iter_previous())
        return sum(1 for _ in skipped)

    def _iter_previous(self):
        lp = self.previous
        while lp is not None:
            yield lp
            lp = lp.previous


if __name__ == "__main__":
    g = GlobalParams(1.5, 100, 3, 0.5, 0.6, 0.3, 1.2, 120, 200, 2)

    rows = [
        {"doy": 150, "eta": 5.0, "precipitation": 2.0, "r": False},
        {"doy": 151, "eta": 4.5, "precipitation": 1.0, "r": False},
        {"doy": 152, "eta": 5.2, "precipitation": 0.0, "r": True},  # after 2 skips
        {"doy": 153, "eta": 4.8, "precipitation": 0.5, "r": True},  # no skips before
    ]

    prev = None
    days = []
    for row in rows:
        lp = LocalParams(
            g, row["doy"], row["eta"], row["precipitation"], row["r"], prev
        )
        days.append(lp)
        prev = lp

    for lp in days:
        print(f"doy {lp.doy} → r={lp.r}, f={lp.f}")
