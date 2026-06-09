class Solution {
    public long maxTotalValue(int[] nums, int k) {
        int mx = nums[0];
        int mn = nums[0];

        for (int x : nums) {
            mx = Math.max(mx, x);
            mn = Math.min(mn, x);
        }

        return 1L * k * (mx - mn);
    }
}