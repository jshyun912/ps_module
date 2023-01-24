!분할정복을 이용한 거듭제곱

!나머지 연산 없는 버전
function pow(a, b) result(res)
    implicit none
    integer*16 :: a, b, res

    res = 1

    do while (b > 0)
        if (mod(b, 2) /= 0) res = res * a
        a = a * a
        b = b / 2
    end do

    return
end

!나머지 연산 있는 버전

function pow(a, b, c) result(res)
    implicit none
    integer*16 :: a, b, c, res

    res = 1

    do while (b > 0)
        if (mod(b, 2) /= 0) res = mod(res * a, c)
        a = mod(a * a, c)
        b = b / 2
    end do

    return
end
