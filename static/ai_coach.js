const sendbtn = document.getElementById('sendBtn');
const userInput = document.getElementById('userInput');
const chatWindow = document.getElementById('chatWindow');

sendbtn.addEventListener('click', async () => {
    const message = userInput.value.trim(); // Get and trim user input

    // Validate input
    if (!message) {
    alert('Please enter a question for the AI.');
    return;
    }

    const userMessage = document.createElement('div');
    userMessage.className = 'bg-gray-200 p-4 rounded-lg shadow-md';
    userMessage.innerText = message;
    chatWindow.appendChild(userMessage);
    userInput.value = ''; // Clear input field

    // Send user question to the server
    try {
        const response = await fetch('/ask_ai', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: message })
        });
        // Check for server errors
        if (!response.ok) {
            console.error('Server error:', response.statusText);
            alert('Server returned8: ' + response.statusText);
            return;
        } 
        // Parse JSON response
        const data = await response.json();

        //Catch JSON parsing errors
        if (data.error) {
            console.error('JSON/API error:', data.error);
            alert('Error from AI: ' + data.error);
            return;
        }

        // Display AI response in chat window
        const aiMessage = document.createElement('div');
        aiMessage.className = 'bg-blue-100 p-4 rounded-lg shadow-md';
        aiMessage.innerText = data.answer.text || data.answer;
        chatWindow.appendChild(aiMessage);


        chatWindow.scrollTop = chatWindow.scrollHeight;
    } catch (error) {
        console.error('Network or JS Error:', error);
        alert('An error occurred while fetching data. Please try again.');
    }
});