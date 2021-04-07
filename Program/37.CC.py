'''
Your task is to convert an input number into an output string. The output strings will be primary colors that correspond to certain potential factors. A factor is a number that evenly divides into another number, leaving no remainder. 
The rules for colors are that if the input number:
- has 5 as a factor, the word "Red" should be print.
- has 7 as a factor, the word "Blue" should be print.
- has 9 as a factor, the word "Yellow" should be print.
- does not have any of 5, 7, or 9 as a factor, the word "Black" should be print.
All input numbers should be cast to an integer, if the input is not a number, an exception should handle it and all that should be print is the value of the error variable provided
## Examples
- 18 has 9 as a factor, but not 5 or 7, so the print would be "Yellow".
- 35 has both 5 and 7 as factors, but not 9, so the result would be "RedBlue".
- 34 is not factored by 5, 7, or 9, so the result would be "Black"
## Important Notes 
- *When multiple colors are print, the color order should be from lowest numbered color to highest*
- *Do not change the input message or error message* 
- *Do not print out anything other than the error or the colour answer* 
- *Outputs with multiple colours should have no spaces or new lines between colour words*
## Example Outputs
`Enter a number: 18` 
`Yellow`
`Enter a number: 35` 
`RedBlue`
`Enter a number: 34`
`Black``
'''


def print_color(num):
    color = ""
    if num % 5 == 0:
        color += "Red"
    if num % 7 == 0:
        color += "Blue"
    if num % 9 == 0:
        color += "Yellow"
    if color == "":
        color = "Black"
    print(color)


try:
    num = int(input("Enter a Number: "))
    print_color(num)

except ValueError:
    print("value of the error variable provided")
