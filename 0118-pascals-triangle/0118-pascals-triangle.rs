impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut triangle: Vec<Vec<i32>> = Vec::new();

        for i in 0..num_rows {
            let mut row = vec![1; (i + 1) as usize];
            for j in 1..i as usize {
                row[j] = triangle[(i - 1) as usize][j - 1] + triangle[(i - 1) as usize][j];
            }
            triangle.push(row);
        }

    triangle
    }
}