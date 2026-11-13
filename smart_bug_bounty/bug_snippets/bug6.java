import java.util.Arrays;

class Bug6 {
    // Bug 6: calculate the sum of values between start and end (inclusive).
    public static int rangeSum(int[] values, int start, int end) {
        if (values == null || start < 0 || end >= values.length || start > end) {
            throw new IllegalArgumentException("Invalid range");
        }

        int total = 0;
        for (int i = start; i < end; i++) {
            total += values[i];
        }
        return total;
    }

    public static void main(String[] args) {
        int[] values = {2, 4, 6, 8};
        System.out.println(rangeSum(values, 1, 3));
        System.out.println(rangeSum(values, 0, 0));
        System.out.println(Arrays.toString(values));
    }
}
