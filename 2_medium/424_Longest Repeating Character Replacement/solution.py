class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # check if we can replace the characters in the current window to make all characters the same
            # `(r - l + 1) - max(count.values()) > k` means that we need to replace more than `k` characters to make all characters the same in the current window, so we need to shrink the window from the left
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res