// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::collections::VecDeque;
use std::cell::RefCell;
impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut result = Vec::new();
        
        if let Some(node) = root {
            let mut queue = VecDeque::new();
            queue.push_back(node);
            
            while !queue.is_empty() {
                let level_size = queue.len();
                let mut level_nodes = Vec::new();
                
                for _ in 0..level_size {
                    if let Some(curr) = queue.pop_front() {
                        let curr_node = curr.borrow();
                        level_nodes.push(curr_node.val);
                        
                        if let Some(left_child) = &curr_node.left {
                            queue.push_back(Rc::clone(left_child));
                        }
                        
                        if let Some(right_child) = &curr_node.right {
                            queue.push_back(Rc::clone(right_child));
                        }
                    }
                }
                
                result.push(level_nodes);
            }
        }
        
        result
    }
}
