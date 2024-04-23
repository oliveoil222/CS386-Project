// Get the edit buttons
const editButtons = document.querySelectorAll('.edit-btn');

// Get the edit modal
const editModal = document.getElementById('edit-modal');

// Get the save button
const saveButton = document.getElementById('save-btn');

// Add event listener to each edit button
editButtons.forEach((button) => {
  button.addEventListener('click', () => {
    // Get the incident id
	const incidentId = button.getAttribute('data-id');

    // Show the edit modal
    editModal.style.display = 'block';

    // Set the incident id in the modal
    editModal.setAttribute('data-id', incidentId);

	let incidentName = button.getAttribute('data-name');
	let incidentDescription = button.getAttribute('data-description');
	let incidentWorker = button.getAttribute('data-worker');
	let incidentDevice = button.getAttribute('data-device');
	let incidentClient = button.getAttribute('data-client');
	let incidentTeam = button.getAttribute('data-team');

	
	// pass the incident name and description the text boxes to be autofilled
	document.getElementById('incident-name').value = incidentName;
	document.getElementById('incident-description').value = incidentDescription;
	document.getElementById('incident-worker').value = incidentWorker;
	document.getElementById('incident-device').value = incidentDevice;
	document.getElementById('incident-client').value = incidentClient;
	document.getElementById('incident-team').value = incidentTeam;
  });
});

// Add event listener to the save button
saveButton.addEventListener('click', () => {
  // Get the incident id from the modal's data attribute
  const incidentId = editModal.getAttribute('data-id');

  // Get the new incident name and description
  const incidentName = document.getElementById('incident-name').value;
  const incidentDescription = document.getElementById('incident-description').value; 
  const incidentStatus = document.getElementById('incident-status').value;
  const incidentWorker = document.getElementById('incident-worker').value;
  const incidentDevice = document.getElementById('incident-device').value;
  const incidentClient = document.getElementById('incident-client').value;
  const incidentTeam = document.getElementById('incident-team').value;

  // Perform the update operation here (e.g., send the updated incident data to the server)
  // ...

  // Hide the edit modal
  editModal.style.display = 'none';
});