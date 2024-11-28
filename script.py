from pyscript import Element
import micropip
import asyncio

#async and await stuff the website told me to use
async def install_beautifulsoup():
    await micropip.install("beautifulsoup4")

#function to display numerical differences and features of two text inputs
def calculate_results(event):

    #uses the textarea id to gather the text
    text_one = Element("first_text").element.value
    text_two = Element("second_text").element.value

    #the arrays to be filled with each letter individually
    values_one = []
    values_two = []

    for char in text_one:
        #only takes alphabetical characters
        if char.isalpha():
            #converts them to lowercase and their ascii values (-96 so a = 1, b = 2, etc.)
            code_one = ord(char.lower()) - 96 
            #all the characters are appended to the array
            values_one.append(code_one)

    #same deal
    for char in text_two:
        if char.isalpha():
            code_two = ord(char.lower()) - 96  
            values_two.append(code_two)

    #the sum of the array data
    total_one = sum(values_one)
    total_two = sum(values_two)
    #the average character value rounded to 3 decimal places
    average_one = round(total_one / len(values_one), 3)
    average_two = round(total_two / len(values_two), 3)
    
    result_one = f"Text One's Value: {total_one}"
    result_two = f"Text Two's Value: {total_two}"

    difference = f"The Difference Between the Two Texts is {total_one - total_two}"

    average_one = f"The Average Character Value of Text One is {average_one}"
    average_two = f"The Average Character Value of Text Two is {average_two}"

    #some cool pyscript features
    output_element = Element("output")
    output_element.write(f"{result_one}, {result_two}")
    difference_element = Element("difference")
    difference_element.write(difference)
    average_element = Element("average")
    average_element.write(f"{average_one}, {average_two}")

#async and await stuff the website told me to use
async def main():
    #async and await stuff the website told me to use
    await install_beautifulsoup()

    #upon button press the results are printed
    button = Element("print_button")
    button.element.onclick = calculate_results
#i honestly do not know what a coroutine is
asyncio.ensure_future(main())