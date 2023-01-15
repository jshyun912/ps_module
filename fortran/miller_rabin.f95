function miller_rabin(a) result(res)
    integer (kind = 16) a, n, k, temp, i, pow
    dimension n(3)
    logical res

    res = .true.

    n = [2, 7, 61]
    
! 1,373,653 = [2, 3] 9,080,191 = [31, 73] 4,759,123,141 = [2, 7, 61] 2,152,302,898,747 = [2, 3, 5, 7, 11]
! 3,474,749,660,383 = [2, 3, 5, 7, 11, 13] 341,550,071,728,321 = [2, 3, 5, 7, 11, 13, 17]
! 숫자 범위에 따라 3번째 배열 및 13번째 do문 수정 필요

    do 10 i = 1, 3, 1
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
    10 continue

    return
end
