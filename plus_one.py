def plusOne(digits):
        total= ''
        for digit in digits:
            total += str(digit)
        total = int(total) + 1


        return [int(digit) for digit in str(total)]
        
