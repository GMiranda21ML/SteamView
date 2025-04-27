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

    data.games.forEach((game, index) => {
      const card = document.createElement('div');
      card.classList.add('game-card');
      card.style.animation = "fadeIn 0.5s ease";  // Adiciona animação leve
      card.innerHTML = `
        <a href="/jogo/${encodeURIComponent(game.name)}" style="text-decoration: none; color: inherit;">
          <div class="ranking-container">
            <div class="ranking">#${(page - 1) * 10 + index + 1}</div>
          </div>
          <img src="${game.image}" alt="${game.name}">
          <div class="game-info">
            <h3>${game.name}</h3>
          </div>
          <div class="game-details">
            <span class="game-rating">Nota: ${game.rating}</span>
            <span class="game-price">${game.price}</span>
          </div>
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

card.style.animation = "fadeIn 0.5s ease";  

