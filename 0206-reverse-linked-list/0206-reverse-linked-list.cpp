/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        return reverseListH(head, nullptr);
    }
    
    ListNode* reverseListH(ListNode* current, ListNode* prev) {
        if (current == nullptr)
            return prev;
        ListNode* nextNode = current->next;
        current->next = prev;
        return reverseListH(nextNode, current);
    }
};