# Laboratory A: the ambiguous SSA case
A <- 30 * pi / 180; a <- 7; b <- 10
s <- b * sin(A) / a
if (abs(s) > 1) { print("No triangle") } else {
  B_candidates <- c(asin(s), pi - asin(s))
  for (B in B_candidates) {
    C <- pi - A - B
    if (C > 0) {
      c_side <- a * sin(C) / sin(A)
      cat(sprintf("B=%.2f deg, C=%.2f deg, c=%.3f\n",
                  B*180/pi, C*180/pi, c_side))
    }
  }
}
