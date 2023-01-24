!병합 정렬 (nlogn)

! 128BIT

subroutine merge_(ary, size, s, m, e)
    implicit none
    integer :: s, m, e, i, j, k
    integer*16 size, ary(size), temp(size)

    i = s; j = m + 1; k = s

    do while ((i <= m) .and. (j <= e))
        if (ary(i) < ary(j)) then
            temp(k) = ary(i)
            i = i + 1
        else
            temp(k) = ary(j)
            j = j + 1
        end if 
        k = k + 1
    end do

    do while (i <= m)
        temp(k) = ary(i)
        k = k + 1; i = i + 1
    end do

    do while (j <= e)
        temp(k) = ary(j)
        k = k + 1; j = j + 1
    end do

    do i = s, e
        ary(i) = temp(i)
    end do
end

recursive subroutine sort(ary, size, s, e)
    implicit none
    integer :: s, e, m
    integer*16 size, ary(size)

    if (s == e) return

    m = (s + e) / 2

    call sort(ary, size, s, m)
    call sort(ary, size, m + 1, e)
    call merge_(ary, size, s, m, e)
end

! 64BIT

subroutine merge_(ary, size, s, m, e)
    implicit none
    integer :: s, m, e, i, j, k
    integer*8 size, ary(size), temp(size)

    i = s; j = m + 1; k = s

    do while ((i <= m) .and. (j <= e))
        if (ary(i) < ary(j)) then
            temp(k) = ary(i)
            i = i + 1
        else
            temp(k) = ary(j)
            j = j + 1
        end if 
        k = k + 1
    end do

    do while (i <= m)
        temp(k) = ary(i)
        k = k + 1; i = i + 1
    end do

    do while (j <= e)
        temp(k) = ary(j)
        k = k + 1; j = j + 1
    end do

    do i = s, e
        ary(i) = temp(i)
    end do
end

recursive subroutine sort(ary, size, s, e)
    implicit none
    integer :: s, e, m
    integer*8 size, ary(size)

    if (s == e) return

    m = (s + e) / 2

    call sort(ary, size, s, m)
    call sort(ary, size, m + 1, e)
    call merge_(ary, size, s, m, e)
end

! 32BIT

subroutine merge_(ary, size, s, m, e)
    implicit none
    integer :: s, m, e, i, j, k
    integer size, ary(size), temp(size)

    i = s; j = m + 1; k = s

    do while ((i <= m) .and. (j <= e))
        if (ary(i) < ary(j)) then
            temp(k) = ary(i)
            i = i + 1
        else
            temp(k) = ary(j)
            j = j + 1
        end if 
        k = k + 1
    end do

    do while (i <= m)
        temp(k) = ary(i)
        k = k + 1; i = i + 1
    end do

    do while (j <= e)
        temp(k) = ary(j)
        k = k + 1; j = j + 1
    end do

    do i = s, e
        ary(i) = temp(i)
    end do
end

recursive subroutine sort(ary, size, s, e)
    implicit none
    integer :: s, e, m
    integer size, ary(size)

    if (s == e) return

    m = (s + e) / 2

    call sort(ary, size, s, m)
    call sort(ary, size, m + 1, e)
    call merge_(ary, size, s, m, e)
end
