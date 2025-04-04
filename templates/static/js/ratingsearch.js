let page = 1;
let loading = false;

async function fetchGames() {
  if (loading) return;
  loading = true;

  try {
    const response = await fetch(`/ratingsearch/api/?page=${page}`);
    const data = await response.json();
    const container = document.getElementById('games-container');

    data.games.forEach(game => {
      const card = document.createElement('div');
      card.classList.add('game-card');
      card.innerHTML = `
        <img src="${game.image}" alt="${game.name}" style="width: 100%; border-radius: 8px;">
        <h4>${game.name}</h4>
        <p>Nota: ${game.rating}</p>
        <p><strong>${game.price}</strong></p>
      `;
      container.appendChild(card);
    });

    page += 1;
  } catch (error) {
    console.error('Erro ao buscar jogos:', error);
  }

  loading = false;
}

fetchGames();

document.getElementById('games-container').addEventListener('scroll', function () {
  const container = this;
  if (container.scrollLeft + container.clientWidth >= container.scrollWidth - 20) {
    fetchGames();
  }
});
