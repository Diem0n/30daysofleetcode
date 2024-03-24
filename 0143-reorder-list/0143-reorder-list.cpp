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
    void reorderList(ListNode* head) {
                if (!head || !head->next)
            return;

        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        std::stack<ListNode*> secondHalf;
        ListNode* curr = slow->next;
        while (curr) {
            secondHalf.push(curr);
            curr = curr->next;
        }
        curr = head;
        while (!secondHalf.empty()) {
            ListNode* nextNode = curr->next;
            ListNode* reversedNode = secondHalf.top();
            secondHalf.pop();
            curr->next = reversedNode;
            reversedNode->next = nextNode;
            curr = nextNode;
        }
        if (curr)
            curr->next = nullptr;
    }

    
};