!밀러 라빈 소수판정법

function miller_rabin(a) result(res)
    integer*16 a, m, k, temp, i, pow
    integer*16, dimension(15) :: n
    logical res

    res = .true.
    
    m = 12
    n(1:m) = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    do i = 1, m, 1
        if (n(i) == a) exit

        if (mod(a, n(i)) == 0) then
            res = .false.
            return
        end if

        k = a - 1

        do while (.true.)
            temp = pow(n(i), k, a)
            
            if (temp == a - 1) exit

            if (mod(k, 2) == 1) then
                if ((temp == 1) .or. (temp == a - 1)) then
                    exit
                else
                    res = .false.
                    return
                end if
            end if
            k = k / 2
        end do
    end do

    return
end
