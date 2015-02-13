#include <stdio.h>

inline int max(int i1, int i2)
{
    return (i1 > i2) ? i1 : i2;
}

// Runtime: O(n)
// New memory used: O(1), assume we can modify the array
int best_heist(int values[], int len)
{

#ifdef DEBUG
    printf("best_heist input:\t");
    for (int i = 0; i < len; ++i) printf("%d\t", values[i]);
    printf("\n");
#endif

    if (len == 0) return 0;   //empty street, boring!
    if (len == 1) return values[0];

    // run our one-dimensional dynamic algorithm
    for (int i = 2; i < len; ++i) {
        if (len == 2) {
            // need this case to avoid indexing into values[-1]
            values[i] += values[0];
            continue;
        }
        values[i] = values[i] + max(values[i-3], values[i-2]); 
    }

#ifdef DEBUG
    printf("best_heist sums:\t");
    for (int i = 0; i < len; ++i) printf("%d\t", values[i]);
    printf("\n");
#endif

    return max(values[len-1], values[len-2]);
}

#ifdef TESTS
void run_tests()
{
    printf("Running extra tests\n");

}
#endif

int main(void)
{
    printf(" = = = Switch.co interview problem = = = \n");

    const int street_size = 5;
    int street1[street_size] = {20, 10, 50, 5, 1};
    int street2[street_size] = {20, 50, 10, 1, 5};

    printf("street1 max: %d\n", best_heist(street1, street_size));
    printf("street2 max: %d\n", best_heist(street2, street_size));

    run_tests();
}
