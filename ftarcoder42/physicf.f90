module physicf
implicit none
contains

    subroutine gmag(m1, m2, r, force_mag)
        use constants
        implicit none
        real, intent(in)    :: m1, m2, r
        real, intent(out)   :: force_mag

        force_mag = G*m1/r/r*m2
        return
    end subroutine gmag

    subroutine force_gravity(nd, m1, m2, r1, r2, f)
        use mathf
        implicit none
        integer, intent(in) :: nd
        real, intent(in)    :: m1, m2
        real, intent(in), dimension(nd)  ::  r1, r2
        real, intent(out) ::  f(nd)
        real, dimension(nd) :: rel
        real    :: g_mag, r_mag

        rel = r2 - r1
        call mag(nd, rel, r_mag)
        call gmag(m1, m2, r_mag, g_mag)
        call unit(nd, rel, f)
        f = f * g_mag

        return
    end subroutine force_gravity

    subroutine net_force(n, nd, masses, positions, forces)
        implicit none
        integer, intent(in) :: n, nd
        real, intent(in), dimension(n)      :: masses
        real, intent(in), dimension(n, nd)   :: positions
        real, intent(out), dimension(n, nd)  :: forces
        real, dimension(nd)  :: force
        integer     :: i, j

        do i=1, n
            do j=1, nd
                forces(i, j) = 0.
            end do
        end do

        do i=1, n
            do j=1, n
                if (i /= j) then
                    call force_gravity(nd, masses(i), masses(j), positions(i, :),&
                                       positions(j, :), force)
                    forces(i, :) = forces(i, :) + force(:)
                end if
            end do
        end do
    end subroutine net_force

    subroutine leapfrog(n, nd, ipos, ivel, masses, dt, fpos, fvel)
        implicit none
        integer, intent(in) :: n, nd
        real, intent(in), dimension(n, nd)    ::  ipos, ivel
        real, intent(in), dimension(n)    :: masses
        real, intent(in)    :: dt
        integer     ::  i
        real, dimension(n, nd)   :: forces, hvel, accels
        real, intent(out), dimension(n, nd)   :: fpos, fvel

        call net_force(n, nd, masses, ipos, forces)
        do i=1, n
            accels(i, :) = forces(i, :) / masses(i)
        end do

        hvel(:, :) = ivel(:, :) + dt/2.*accels(:, :)

        fpos(:, :) = ipos(:, :) + hvel(:, :)*dt

        call net_force(n, nd, masses, fpos, forces)
        do i=1, n
            accels(i, :) = forces(i, :) / masses(i)
        end do
        fvel(:, :) = hvel(:, :) + 0.5*dt*accels(:, :)

    end subroutine leapfrog

end module physicf