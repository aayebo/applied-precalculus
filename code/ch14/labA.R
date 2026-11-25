# Laboratory A: vectors and projections
u <- c(4, 3)
v <- c(2, 1)
dot <- sum(u * v)
angle <- acos(dot / (sqrt(sum(u^2)) * sqrt(sum(v^2))))
projection <- dot / sum(v^2) * v
residual <- u - projection
print(list(angle_degrees=angle*180/pi, projection=projection, residual=residual, orthogonality=sum(residual*v)))
plot(c(0,u[1],v[1],projection[1]), c(0,u[2],v[2],projection[2]), type="n", xlim=c(0,5), ylim=c(0,4), asp=1, xlab="x", ylab="y", main="Vectors and projection")
arrows(0,0,u[1],u[2],col="blue",lwd=2); arrows(0,0,v[1],v[2],col="red",lwd=2); arrows(0,0,projection[1],projection[2],col="darkgreen",lwd=2)
