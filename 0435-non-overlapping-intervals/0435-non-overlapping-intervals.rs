impl Solution {
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
    if intervals.is_empty() {
        return 0;
    }

    let mut sorted_intervals = intervals;
    sorted_intervals.sort_by_key(|interval| interval[1]);

    let mut count = 0;
    let mut end = sorted_intervals[0][1];

    for i in 1..sorted_intervals.len() {
        if sorted_intervals[i][0] < end {
            count += 1;
        } else {
            end = sorted_intervals[i][1];
        }
    }

    count
    }
}