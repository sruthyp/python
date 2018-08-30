class py_solution:
    def roman_to_int(self, s):
        rom_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_values = 0
        for i in range(len(s)):
            if i > 0 and rom_values[s[i]] > rom_values[s[i - 1]]:
                int_values += rom_values[s[i]] - 2 * rom_values[s[i - 1]]
            else:
                int_values += rom_values[s[i]]
        return int_values

print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('C'))
