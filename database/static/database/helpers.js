const discount = 0.1;
const discount_cap = 0.6;

function get_seminar_checkboxes() {
  return document.querySelectorAll('[id^="seminarCheckBox"]');
}

function get_package_checkboxes() {
  return document.querySelectorAll('[id^="packageCheckBox"]');
}

function get_ticked_seminar_checkboxes() {
  let tickedCheckboxes = [];

  let seminar_checkboxes = get_seminar_checkboxes();
  for (let i = 0; i < seminar_checkboxes.length; ++i) {
    let checkbox = seminar_checkboxes[i];
    if (checkbox.checked) tickedCheckboxes.push(checkbox);
  }

  return tickedCheckboxes;
}

function get_ticked_package_checkboxes() {
  let tickedCheckboxes = [];

  let package_checkboxes = get_package_checkboxes();
  for (let i = 0; i < package_checkboxes.length; ++i) {
    let checkbox = package_checkboxes[i];
    if (checkbox.checked) tickedCheckboxes.push(checkbox);
  }

  return tickedCheckboxes;
}

function get_ticked_checkboxes() {
  let tickedCheckboxes = get_ticked_seminar_checkboxes();
  let ticked_package_checkboxes = get_ticked_package_checkboxes();

  for (let i = 0; i < ticked_package_checkboxes.length; ++i) {
    let checkbox = ticked_package_checkboxes[i];
    tickedCheckboxes.push(checkbox);
  }

  return tickedCheckboxes;
}

function get_total_cost(tickedCheckboxes) {
  let totalCost = 0.0;

  for (let i = 0; i < tickedCheckboxes.length; i++) {
    let checkboxCost = parseFloat(
      tickedCheckboxes[i].getAttribute("data-price")
    );
    totalCost += checkboxCost;
  }

  return totalCost.toFixed(2);
}

function reset_payment_button() {
  const button = document.getElementById("paymentButton");
  const text = document.getElementById("paymentText");

  let tickedCheckboxes = get_ticked_checkboxes();

    if (tickedCheckboxes.length > 0) {
        let total_cost = get_total_cost(tickedCheckboxes)

    button.disabled = false;
    text.textContent = "Total cost: R" + total_cost;
    button.className = "btn-grad";
  } else {
    button.disabled = true;
    text.textContent = "Please select at least one seminar/package";
    button.className = "btn-grad";
  }
}

function uuidv4() {
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
    var r = (Math.random() * 16) | 0,
      v = c == "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

function get_all_chosen_seminars() {
  if (get_ticked_package_checkboxes().length > 0) {
    let ticked_package_checkboxes = get_ticked_package_checkboxes();
    let chosen_seminars = ticked_package_checkboxes[0].getAttribute("data-id")
    for (let i = 1; i < ticked_package_checkboxes.length; i++) {
      chosen_seminars += "," + ticked_package_checkboxes[i].getAttribute("data-id");
    }
    return chosen_seminars;
  }

  else if (get_ticked_seminar_checkboxes().length > 0) {
    let ticked_seminar_checkboxes = get_ticked_seminar_checkboxes();
    let chosen_seminars = ticked_seminar_checkboxes[0].getAttribute("data-id")
    for (let i = 1; i < ticked_seminar_checkboxes.length; i++) {
      chosen_seminars += "," + ticked_seminar_checkboxes[i].getAttribute("data-id");
    }
    return chosen_seminars;
  }

  return "";
}

function generate_payment_info() {
  const amount_field = document.getElementsByName("amount")[0];
  const item_name_field = document.getElementsByName("item_name")[0];
  const m_payment_id_field = document.getElementsByName("m_payment_id")[0];
  const custom_str1_field = document.getElementsByName("custom_str1")[0]; // For student details
  const custom_str2_field = document.getElementsByName("custom_str2")[0]; // For covid acceptance
  const custom_str3_field = document.getElementsByName("custom_str3")[0]; // For chosen seminars
  const custom_str4_field = document.getElementsByName("custom_str4")[0]; // For additional info
  const custom_str5_field = document.getElementsByName("custom_str5")[0]; // For parent cell number

  // Calculate the total amount
  let tickedCheckboxes = get_ticked_checkboxes();
  let total_cost = get_total_cost(tickedCheckboxes);

  // Payment ID
  let payment_id = uuidv4();

  // Student details
  const student_first_name_field = document.getElementById("studentFirstName");
  const student_last_name_field = document.getElementById("studentLastName");
  const student_email_field = document.getElementById("studentEmail");
  const student_phone_number_field =
    document.getElementById("studentPhoneNumber");
  let student_information =
    student_first_name_field.value +
    "," +
    student_last_name_field.value +
    "," +
    student_email_field.value +
    "," +
    student_phone_number_field.value;

  // Covid acceptance
  const parent_covid_acceptance = document.getElementById("parentCovidWaiver");
  const student_covid_acceptance =
    document.getElementById("studentCovidWaiver");
  let covid_info =
    parent_covid_acceptance.checked + "," + student_covid_acceptance.checked;

  // Chosen seminars
  let seminar_info = get_all_chosen_seminars();

  // Additional info
  const additional_info_field = document.getElementById(
    "additionalInfoTextArea"
  );

  // Cell number
  const cell_number = document.getElementById("cell_number");

  amount_field.value = total_cost;
  item_name_field.value =
    "Registration fee for " + seminar_info.split(",").length + " seminar(s)";
  m_payment_id_field.value = payment_id;
  custom_str1_field.value = student_information;
  custom_str2_field.value = covid_info;
  custom_str3_field.value = seminar_info;
  custom_str4_field.value = additional_info_field.value;
  custom_str5_field.value = cell_number.value;
}

function reset_checkboxes() {
  let seminarCheckboxes = get_seminar_checkboxes()
  for (let i = 0; i < seminarCheckboxes.length; ++i) {
    let checkbox = seminarCheckboxes[i];
    checkbox.checked = false;
  }

  let packageCheckboxes = get_package_checkboxes()
  for (let i = 0; i < packageCheckboxes.length; ++i) {
    let checkbox = packageCheckboxes[i];
    checkbox.checked = false;
  }
  reset_payment_button()
}
