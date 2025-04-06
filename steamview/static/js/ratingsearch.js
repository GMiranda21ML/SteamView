let page = 1;
let loading = false;

async function fetchGames() {
  if (loading) return;
  loading = true;

  try {
    const response = await fetch(`/ratingsearch/api/?page=${page}`);
    const data = await response.json();
    const container = document.getElementById('games-container');

    if (!data.has_next || data.games.length === 0) {
        document.getElementById('load-more').style.display = 'none';
    }
      
    data.games.forEach(game => {
      const card = document.createElement('div');
      card.classList.add('game-card');
      card.innerHTML = `
      <a href="/jogo/${encodeURIComponent(game.name)}" style="text-decoration: none; color: inherit;">
        <img src="${game.image}" alt="${game.name}" style="width: 100%; border-radius: 8px;">
        <h4>${game.name}</h4>
        <p>Nota: ${game.rating}</p>
        <p><strong>${game.price}</strong></p>
      </a>
      `;    
      container.appendChild(card);
    });

    page += 1;
  } catch (error) {
    console.error('Erro ao buscar jogos:', error);
  }

  loading = false;
}

// Primeira chamada automática
fetchGames();

// Botão "Mostrar mais"
document.getElementById('load-more').addEventListener('click', fetchGames);
