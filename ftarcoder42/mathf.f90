module mathf
    implicit none
    contains

    subroutine mag(n, a, a_mag)
        implicit none
        integer, intent(in) :: n
        real, intent(in)    :: a(n)
        real, intent(out)   :: a_mag
        a_mag = sqrt(sum(a**2))
        return
    end subroutine mag

    subroutine unit(n, a, a_unit)
        implicit none
        integer, intent(in) :: n
        real, intent(in)    :: a(n)
        real, intent(out)   :: a_unit(n)
        real    :: a_mag
        call mag(n, a, a_mag)
        a_unit = a / a_mag
        return
    end subroutine unit

    subroutine find_gcd(a, b, gcd)
        implicit none
        integer, intent(in)     :: a, b
        integer                 :: c, d
        integer, intent(out)    :: gcd
        c = a
        gcd = b
        do while (c /= 0)
            d = c
            c = modulo(gcd, c)
            gcd = d
        end do
    end subroutine find_gcd

    subroutine mandelbrot_set(z, c, n, n_iter, z_f)
        implicit none
        integer, intent(in) :: n, n_iter
        complex, intent(in), dimension(n, n) :: z, c
        complex, intent(out), dimension(n, n) :: z_f
        integer :: i
        z_f = z
        do i=1, n_iter
            z_f = z_f**2 + c
        end do
    end subroutine mandelbrot_set

    subroutine mandelbrot_rate(z, c, n, n_iter, z_f)
        implicit none
        integer, intent(in) :: n, n_iter
        complex, intent(in), dimension(n, n) :: z, c
        complex, intent(out), dimension(n_iter + 1, n, n) :: z_f
        integer :: i
        z_f(1, :, :) = z(:, :)
        do i=1, n_iter
            z_f(i+1, :, :) = z_f(i, :, :)**2 + c
        end do
    end subroutine mandelbrot_rate

end module mathf
