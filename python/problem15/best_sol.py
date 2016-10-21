g = 20;
paths = 1;
 
for i in range( 0, g):
    paths = paths * ((2 * g) - i);
    paths = paths / (i + 1);

print paths
