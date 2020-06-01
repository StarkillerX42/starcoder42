module ffitsio
   ! None of this works
    implicit none
    contains

    subroutine get_header(filename, dict_keys, dict_items)
        implicit none
        character(*), intent(in)    :: filename
        character(8), dimension(:), intent(out)  :: dict_keys
        real, dimension(:), intent(out) :: dict_items
        character(*), pointer :: header
!        integer :: i
        dict_keys(1) = '        '
!        open(10, file=filename, status='old')
!        allocate(header)
!        read(10, *) header
!        do i=1, len(header)/80
!            print *, header((i-1)*80:(i-1)*80+8)
!        end do
    end subroutine get_header
end module ffitsio