function updateInputFields() {
    const count = document.getElementById('urlCount').value;
    const inputFieldsContainer = document.getElementById('inputFields');

    // Clear previous input fields
    inputFieldsContainer.innerHTML = '';

    // Populate input fields based on count
    for (let i = 0; i < count; i++) {
        const input = document.createElement('input');
        input.type = 'text';
        input.placeholder = `Enter Instagram Reel URL ${i + 1}`;
        input.className = 'reelUrl'; // Optional: add a class for styling or selection
        inputFieldsContainer.appendChild(input);
    }
}

function downloadAndUpload() {
    const urls = [];
    const count = document.getElementById('urlCount').value;

    // Check if count is valid
    if (count < 1 || count > 10) {
        document.getElementById('status').innerText = "Please enter a valid number of URLs (1-10).";
        return;
    }

    // Collect all URLs from the dynamically created input fields
    const inputs = document.querySelectorAll('.reelUrl');
    inputs.forEach(input => {
        if (input.value) {
            urls.push(input.value);
        }
    });

    // Proceed to send the URLs to the backend
    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ count: urls.length, urls: urls }),
    })
    .then(response => {
        // Check the Content-Type of the response
        const contentType = response.headers.get('Content-Type');
    
        if (contentType && contentType.includes('text/html')) {
            // If the response is HTML, it might be a login page
            // Redirect the user to the login page with the next parameter
            window.location.href = '/login?next=/download';
            throw new Error('User not logged in. Redirecting to login page...');
        }
    
        // Check if the response is JSON (as we expect JSON response)
        if (contentType && contentType.includes('application/json')) {
            // Proceed if the response is JSON, parse it
            return response.json();
        }
    
        // Handle any other unexpected content type
        throw new Error('Unexpected content type: ' + contentType);
    })
    .then(data => {
        // If the download is successful, handle the completion and call upload
        document.getElementById('status').innerText = data.message;
    
        // Now that the download is successful, call upload
        return fetch('/upload', { method: 'POST' });
    })
    .then(response => {
        // Check the Content-Type of the upload response
        const contentType = response.headers.get('Content-Type');
    
        if (contentType && contentType.includes('text/html')) {
            // If the response is HTML, it might be a login page
            // Redirect the user to the login page with the next parameter
            window.location.href = '/login?next=/upload';
            throw new Error('User not logged in. Redirecting to login page...');
        }
    
        // If the response is JSON, proceed
        if (contentType && contentType.includes('application/json')) {
            return response.json();
        }
    
        // Handle any unexpected content type
        throw new Error('Unexpected content type: ' + contentType);
    })
    .then(data => {
        // Display success message from upload
        document.getElementById('status').innerText = data.message;
    })
    .catch(error => {
        // Handle any errors, including login redirects and network issues
        document.getElementById('status').innerText = "Error: " + error.message;
    });
    
    
}