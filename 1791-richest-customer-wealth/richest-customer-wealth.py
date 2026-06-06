class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            current_customer_wealth = 0
            for money in customer:
                current_customer_wealth += money
            if current_customer_wealth > max_wealth:
                max_wealth = current_customer_wealth
        return max_wealth
                
        