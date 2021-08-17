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

    let tickedCheckboxes = get_ticked_checkboxes()

    let has_selected_one_checkbox = tickedCheckboxes.length > 0

    if (has_selected_one_checkbox) {
        let total_cost = get_total_cost(tickedCheckboxes)

        button.disabled = false;
        text.textContent = "Total cost: R" + total_cost
        button.className = "btn btn-success"
    } else {
        button.disabled = true;
        text.textContent = "Please select at least one seminar"
        button.className = "btn btn-secondary"
    }
}

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

function generate_payment_info() {
    const amount_field = document.getElementsByName('amount')[0]
    const item_name_field = document.getElementsByName('item_name')[0];
    const m_payment_id_field = document.getElementsByName('m_payment_id')[0];

    // Calculate the total amount
    let tickedCheckboxes = get_ticked_checkboxes()
    let total_cost = get_total_cost(tickedCheckboxes)

    let payment_id = uuidv4()

    amount_field.value = total_cost
    item_name_field.value = "Registration fee for " + tickedCheckboxes.length + " seminar(s)"
    m_payment_id_field.value = payment_id
}