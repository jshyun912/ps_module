!폴라드 로

function rabit(a, b, c) result (d)
    integer*16 a, b, c, d
    d = mod(mod(a * a, c) + b, c)
    return
end

function pl(a) result (b)
    implicit none
    integer*16 a, b, c, x, y, rabit, gcd, num, xorshift
    logical miller_rabin

    if (a == 1) then
        b = 1
        return
    else if (mod(a, 2) == 0) then
        b = 2
        return
    else if (miller_rabin(a) .eqv. .true.) then
        b = a
        return
    end if

    num = 1
    10 num = xorshift(num)
    x = mod(num, a)
    y = x
    num = xorshift(num)
    c = mod(num, a)
    b = 1

    do while (b == 1)
        if (b == a) goto 10
        x = rabit(x, c, a)
        y = rabit(rabit(y, c, a), c, a)
        b = gcd(abs(x-y), a)
    end do

    if (miller_rabin(b) .eqv. .false.) goto 10
    return 
end
