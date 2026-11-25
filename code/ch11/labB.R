# Laboratory B: navigation and triangulation
d <- c(12, 8); az <- c(60, 150) * pi / 180
east <- sum(d * sin(az)); north <- sum(d * cos(az))
distance <- sqrt(east^2 + north^2)
azimuth <- (atan2(east, north) * 180 / pi) %% 360
cat(sprintf("East=%.3f, North=%.3f km\n", east, north))
cat(sprintf("Distance=%.3f km, azimuth=%.2f deg\n", distance, azimuth))
baseline <- 100; A <- 48*pi/180; B <- 67*pi/180
T <- pi-A-B
cat(sprintf("AT=%.3f m, BT=%.3f m\n",
 baseline*sin(B)/sin(T), baseline*sin(A)/sin(T)))
