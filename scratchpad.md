
axics setpos [-37 -27] pd polystop 52 72 pu

# 5 pointed star 
axics axisetpos [-10 -42] axipd axipolystop 80 144 axipu

# 9 fat star
axics axisetpos [-37 -31] axipd axipolystop 60 80 axipu

# lots of points 
axics axisetpos [-25 -31] axipd axipolystop 60 100 axipu

# 
axics axisetpos [-30 -20] axipd newpoly 30 30 axipu

# star no intersection
axics axisetpos [-10 10] axipd newpoly 30 144 axipu


# sun vibe
axics axisetpos [-20 30] axipd newpoly 10 125 axipu

# two squares
axics axisetpos [-35 -35] axipd newpoly 50 45 axipu


axics axisetpos [-10 0] axipd polyspi 3 120 2 41 axipu

# spiral vibes
axics axisetpos [0 0] axipd polyspi 1 30 0.3 80 axipu

# inward spiral 1, 6 flowers
axics axisetpos [-38 10] axipd inspi 3 20 3 800 axipu

axics axisetpos [0 0] axipd inspi 3 0 7 900 axipu

axics axisetpos [0 0] axipd polyroll 30 90 30 axipu


axics axisetpos [0 0] axipd polyroll 30 144 30 axipu


axics axisetpos [10 -30] axipd lbranch 5 20 7 axipu

cs setpos [-30 0] rt 18 fd 100 rt 144 fd 100 rt 180 - 72 fd 61 rt 90 setpos [0 0]