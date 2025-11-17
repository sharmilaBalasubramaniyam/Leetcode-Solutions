class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length()) return result;

        int[] countP = new int[26];
        int[] window = new int[26];

        for (char c : p.toCharArray())
            countP[c - 'a']++;

        int k = p.length();

        for (int i = 0; i < s.length(); i++) {
            window[s.charAt(i) - 'a']++;

            if (i >= k)
                window[s.charAt(i - k) - 'a']--;
                
            if (Arrays.equals(window, countP))
                result.add(i - k + 1);
        }
        return result;
    }
}
