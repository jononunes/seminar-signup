function get_ticked_checkboxes() {
    let allCheckboxes = document.querySelectorAll('[id^="seminarCheckBox"]')
    let tickedCheckboxes = []

    for (let i = 0; i < allCheckboxes.length; ++i) {
        let checkbox = allCheckboxes[i];
        if (checkbox.checked) tickedCheckboxes.push(checkbox)
    }
    return tickedCheckboxes;
}

function get_total_cost(tickedCheckboxes) {
    let totalCost = 0.0;

    for (let i = 0; i < tickedCheckboxes.length; i++) {
        let checkboxCost = parseFloat(tickedCheckboxes[i].getAttribute("data-price"))
        totalCost += checkboxCost
    }

    return totalCost.toFixed(2)
}

function reset_payment_button() {
    const button = document.getElementById('paymentButton')
    const text = document.getElementById('paymentText')
    const itemName = document.getElementsByName('item_name')[0];
    const amount = document.getElementsByName('amount')[0]
    let tickedCheckboxes = get_ticked_checkboxes()

    let has_selected_one_checkbox = tickedCheckboxes.length > 0

    if (has_selected_one_checkbox) {
        let total_cost = get_total_cost(tickedCheckboxes)

        button.disabled = false;
        text.textContent = "Total cost: R" + total_cost
        button.className = "btn btn-success"
        itemName.value = "Registration fee for " + tickedCheckboxes.length + " seminar(s)"
        amount.value = total_cost

    } else {
        button.disabled = true;
        text.textContent = "Please select at least one seminar"
        button.className = "btn btn-secondary"
        itemName.value = ""
        amount.value = ""
    }
}