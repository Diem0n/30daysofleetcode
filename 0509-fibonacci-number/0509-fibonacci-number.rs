impl Solution {
     pub fn fib(n: i32) -> i32 {
        if n <= 1 {
            return n;
        }
        
        let mut prev = 0;
        let mut curr = 1;
        
        for _ in 2..=n {
            let next = prev + curr;
            prev = curr;
            curr = next;
        }
        
        curr
    }
}