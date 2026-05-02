class Solution {
    public static boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<Character>();
        Map<Character, Character> closeToOpen= new HashMap<Character, Character>();
        closeToOpen.put(')', '(');
        closeToOpen.put('}', '{');
        closeToOpen.put(']', '[');

        for (char c : s.toCharArray()) {
            if (closeToOpen.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == closeToOpen.get(c)) {
                    stack.pop();
                }
                else return false;
            }
            else stack.push(c);
        }

        return stack.isEmpty();        
    }
}
