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
        
        const response =  await fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ salary: Number(salary) })
        });
        const data = await response.json();

        for (const category of data.categories) {
            const card = document.createElement('div');
            card.className = 'bg-white rounded-lg shadow-md p-6 text-center';
            card.innerHTML = `
            <p class="text-lg font-medium">${category}</p>
            <p class="text-gray-700">$${budget[category]}</p>
            `;
            cardsContainer.appendChild(card);
        }
    } catch (error) {
        alert('An error occurred while fetching data. Please try again.');
        return;
    }

});