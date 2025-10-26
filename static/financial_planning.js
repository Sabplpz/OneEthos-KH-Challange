const button = document.getElementById('submitBtn');
const input = document.getElementById('salaryInput');
const cardsContainer = document.getElementById('cardsContainer');

button.addEventListener('click', async () => {
    const salary = input.value.trim();
    cardsContainer.innerHTML = ''; // Clear any existing cards

    if (!salary || isNaN(salary) || Number(salary) <= 0) {
        alert('Please enter a valid salary amount.');
        return;
    }

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ salary: Number(salary) })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        if (!data || !data.categories || !data.budget) {
            throw new Error('Invalid data format received');
        }

        data.categories.forEach(category => {
            const card = document.createElement('div');
            card.className = 'bg-white rounded-lg shadow-md p-6 text-center';
            card.innerHTML = `
                <p class="text-lg font-medium">${category}</p>
                <p class="text-gray-700">$${data.budget[category].toFixed(2)}</p>
            `;
            cardsContainer.appendChild(card);
        });

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while fetching data. Please try again.');
    }
});