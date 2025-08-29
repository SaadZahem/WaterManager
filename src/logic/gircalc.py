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


def find_zr(doy: int, to: int, tx: int, zo: float, zx: float, n: float) -> float:
    if doy < to:
        return zo

    return zo + (zx - zo) * ((doy - to / 2) / (tx - to / 2)) ** (1 / n)


def find_taw_raw(aw: float, zr: float, mad: float) -> tuple[float, float]:
    taw = aw * zr
    raw = taw * mad
    return taw, raw


def find_gir(a, ece, ecw, eta, p):
    di = eta - p
    lr = ecw / (5 * ece - ecw)

    if lr > 0.1:
        dg = di / 0.55 * (1 - lr)
    else:
        dg = di / 0.55

    gir = dg * a * 4200 / 1000

    return gir


if __name__ == "__main__":
    pass
