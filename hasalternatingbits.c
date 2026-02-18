#include <stdbool.h>

bool hasAlternatingBits(int n) {
    int prev_bit = n & 1; // Get the least significant bit
    n >>= 1; // Shift right to process the next bit

    while (n > 0) {
        int current_bit = n & 1; // Get the current least significant bit
        if (current_bit == prev_bit) {
            return false; // If the current bit is the same as the previous bit, return false
        }
        prev_bit = current_bit; // Update previous bit
        n >>= 1; // Shift right to process the next bit
    }

    return true; // All bits are alternating
}