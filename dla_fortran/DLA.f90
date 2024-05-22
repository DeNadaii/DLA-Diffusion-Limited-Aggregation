program  dla


implicit none

real:: x, y, rlan, ragr, rkill, pi,theta, dis,rp
integer:: i, ntotal, cont, flag, contlog,j
real, allocatable, dimension(:)::xdep,ydep

ntotal = 1000
rp = 1.0d0
allocate(xdep(ntotal))
allocate(ydep(ntotal))

pi = 4.0*atan(1.0d0)
open(1, file='dla_off_lattice.dat', status='unknown')

cont=1
ragr = 1.0d0
rlan=  ragr+10
rkill = 10*rlan
xdep = 0
ydep = 0
write(1,*) 0,0
print*,cont
do while(cont<ntotal-1)
	
	call random_number(theta)
	theta = theta*2.0*pi
	x =  rlan*cos(theta)
	y =  rlan*sin(theta)
	flag = 1
	
	do while(flag==1)
		call random_number(theta)
		theta = theta*pi*2.0d0
		x = x + cos(theta)
		y = y + sin(theta)
		i=cont
		contlog=1
		do while(flag==1.and.i>=1.and.contlog==1)
			i=i-1
			if(i==0)then
				i=1
				contlog=2
			end if
			dis = sqrt((x - xdep(i))**2 + (y-ydep(i))**2)
			if(dis<=2.0*rp)then
				flag=2
				cont =cont +1
				xdep(cont)=x
				ydep(cont)=y
				write(1,*) x,y
				print*,cont
				if(sqrt(x**2+y**2)>ragr)then
					ragr = sqrt(x**2+y**2)
					rlan=  ragr+10
					rkill = 10*rlan
				end if
			end if
		end do
		if(sqrt(x**2+y**2)>=rkill)then
			flag=2
		end if	
	end do 
end do	



close(1)
stop
end program dla
