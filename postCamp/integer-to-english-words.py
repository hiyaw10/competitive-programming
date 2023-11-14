class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Define lists for English word representation
        ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']


        # Helper function to recursively build English word representation for a number
        def helper(number):
            if number == 0:
                return ''
            elif number < 10:
                return ones[number]
            elif number < 20:
                return teens[number - 10] # teens[number%10]
            elif number < 100:
                return tens[number // 10] + ' ' + helper(number % 10)
            else:
                return ones[number // 100] + ' Hundred ' + helper(number % 100)

        words = '' 
        i = 0

        # Split the number into groups of three digits (thousands, millions, billions)
        while num > 0:
            if num % 1000 != 0:
                # Get the English word representation for the group using the helper function
                group_words = helper(num % 1000).strip()
                # Append the group representation, along with the corresponding power of thousand, to the result
                words = group_words + ' ' + thousands[i] + ' ' + words
            num //= 1000
            i += 1

        return words.strip()