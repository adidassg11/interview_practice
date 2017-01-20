#  https://www.hackerrank.com/challenges/largest-rectangle
# UNFINISHED WIP - failing due to performance

# Enter your code here. Read input from STDIN. Print output to STDOUT

num_buildings = int(raw_input())
heights = map(int, raw_input().split())

# brute force
max_area = 0
max_area_range = (-1, -1)

for i in xrange(num_buildings):
    for j in xrange(i, num_buildings):
        min_height = min(heights[i:j+1])
        width = j-i+1
        total_area = min_height * width
        if total_area > max_area:
            max_area = total_area
            max_area_range = (i, j)
            #print 'Area update: %s from %s to %s' % (str(max_area), str(i), str(j))
            
print max_area
#print max_area_range
