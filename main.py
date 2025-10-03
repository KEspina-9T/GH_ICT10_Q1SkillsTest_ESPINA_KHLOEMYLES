from pyscript import display, document  # type: ignore #this type: ignore is VS Code's quick fix feature.

def order_calculation(e):
    #I tried using .value but it didn't work, so I did research to use .checked
    item1 = document.getElementById('Jungle Grove Latté')
    item2 = document.getElementById('Mossy Matcha Cheescake')
    item3 = document.getElementById('Flowering Hibuscus Tea')
    item4 = document.getElementById('Rose Petal Tart')
    item5 = document.getElementById('Maple Syrup Waffles')

    total_sum = 0 #this is here so the balance starts at 0
    
    #each time one of the checkbox is checked, this will be the one that will add to the total sum.
    total_sum  = total_sum  + float(item1.value) * item1.checked
    total_sum  = total_sum  + float(item2.value) * item2.checked
    total_sum  = total_sum  + float(item3.value) * item3.checked
    total_sum  = total_sum  + float(item4.value) * item4.checked
    total_sum  = total_sum  + float(item5.value) * item5.checked

    #this one is the one for the information sheet
    name = document.getElementById('name').value
    address = document.getElementById('address').value
    contact = document.getElementById('contact').value

    
    message = f"""
    Name: {name} \n
    Address: {address} \n
    Contact: {contact} \n
    The total of your order is ₱{total_sum }
    """
    display(message, target="output")
