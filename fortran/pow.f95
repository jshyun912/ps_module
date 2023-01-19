!분할정복을 이용한 거듭제곱

function pow(a, b, div) result(res)
    implicit none
    integer*16 a, b, d, e, div, res
    d = a 
    e = b 
    res = 1
    d = mod(d, div)

    do while (e > 0)
        if (mod(e, 2) /= 0) res = mod((d * res), div)
        d = mod(d * d, div)
        e = e / 2
    end do

    return
end
