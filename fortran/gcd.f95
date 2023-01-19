!유클리드 호제법

function gcd(a, b) result(i)
    implicit none
    integer*16 a, b, i, j, temp
    i = a
    j = b

    do while (j > 0)
        temp = i
        i = j
        j = mod(temp, j)
    end do
    
   return 
end
