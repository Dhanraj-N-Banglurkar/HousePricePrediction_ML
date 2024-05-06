// Get all the form elements
const citySelect = document.getElementById('city');
const locationSelect = document.getElementById('location');
const amenitiesList = document.getElementById('amenities-list');
const selectedAmenitiesCount = document.getElementById('selected-amenities-count');
const squareFeetInput = document.getElementById('square-feet');
const bhkInput = document.getElementById('bhk');
const resetBtn = document.querySelector('.reset-btn');
const submitBtn = document.querySelector('.submit-btn');

// Show alert
function showAlert(message) {
  const alertContainer = document.createElement('div');
  alertContainer.className = 'alert';
  alertContainer.innerHTML = `
    <h3>Error</h3>
    <p id="message">${message}</p>
  `;

  document.body.appendChild(alertContainer);

  // Position the alert in the top-right corner of the screen
  alertContainer.style.right = '2rem';
  alertContainer.style.top = '2rem';

  // Hide alert after 3 seconds
  setTimeout(() => {
    alertContainer.remove();
  }, 2000);
}

// Get the selected city and location
citySelect.addEventListener('change', () => {
  console.log(`Selected city: ${citySelect.value}`);
});

locationSelect.addEventListener('change', () => {
  console.log(`Selected location: ${locationSelect.value}`);
});

// Get the selected amenities
const amenityInputs = amenitiesList.getElementsByTagName('input');
let selectedAmenities = [];
for (let i = 0; i < amenityInputs.length; i++) {
  amenityInputs[i].addEventListener('change', () => {
    selectedAmenities = [];
    for (let j = 0; j < amenityInputs.length; j++) {
      if (amenityInputs[j].checked) {
        selectedAmenities.push(amenityInputs[j].id);
      }
    }
    selectedAmenitiesCount.textContent = `Selected amenities: ${selectedAmenities.length}`;
    console.log(`Selected amenities: ${selectedAmenities.join(', ')}`);
  });
}

// Get the entered square feet
squareFeetInput.addEventListener('input', () => {
  console.log(`Entered square feet: ${squareFeetInput.value}`);
});

// Reset the form
resetBtn.addEventListener('click', () => {
  citySelect.selectedIndex = 0;
  locationSelect.selectedIndex = 0;
  for (let i = 0; i < amenityInputs.length; i++) {
    amenityInputs[i].checked = false;
  }
  selectedAmenitiesCount.textContent = 'Selected amenities: 0';
  squareFeetInput.value = '';
});

// Submit the form
submitBtn.addEventListener('click', (e) => {
  e.preventDefault();
  console.log('Form submitted');

  // Check if the input values are within the limits
  if (squareFeetInput.value > 5000 || squareFeetInput.value < 100 || bhkInput.value > 5 || bhkInput.value < 1) {
    showAlert('Please enter a valid value for square feet (min 100 & max 5000) and bhk (max 5).');
    return;
  }
  // Add your form submission logic here
});
