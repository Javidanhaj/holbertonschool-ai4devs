import java.util.Arrays;

class Bug5 {
    // Bug 5: find the largest integer, including all-negative arrays.
    public static int maxValue(int[] values) {
        if (values == null || values.length == 0) {
            throw new IllegalArgumentException("Array must not be empty");
        }

        int largest = 0;
        for (int value : values) {
            if (value > largest) {
                largest = value;
            }
        }
        return largest;
    }

    public static void main(String[] args) {
        System.out.println(maxValue(new int[]{4, 2, 9}));
        System.out.println(maxValue(new int[]{-9, -3, -7}));
        System.out.println(Arrays.toString(new int[]{1, 2, 3}));
    }
}
