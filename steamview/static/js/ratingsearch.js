let page = 1;
let loading = false;
let order = 'desc'; // Começa do melhor para o pior

async function fetchGames(reset = false) {
  if (loading) return;
  loading = true;

  try {
    if (reset) {
      page = 1;
      document.getElementById('games-container').innerHTML = ''; // limpa os cards antigos
    }

    const response = await fetch(`/ratingsearch/api/?page=${page}&order=${order}`);
    const data = await response.json();
    const container = document.getElementById('games-container');

    if (!data.has_next || data.games.length === 0) {
      document.getElementById('load-more').style.display = 'none';
    } else {
      document.getElementById('load-more').style.display = 'block';
    }

    data.games.forEach((game, index) => {
      const card = document.createElement('div');
      card.classList.add('game-card');
      card.style.animation = "fadeIn 0.5s ease";

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

    page += 1; // só incrementa depois de adicionar os jogos
  } catch (error) {
    console.error('Erro ao buscar jogos:', error);
  }

  loading = false;
}

document.addEventListener("DOMContentLoaded", () => {
  fetchGames();

  const loadMoreButton = document.getElementById('load-more');
  if (loadMoreButton) {
    loadMoreButton.addEventListener('click', () => {
      fetchGames();
    });
  }

  const invertButton = document.getElementById('invert-order');
  if (invertButton) {
    invertButton.addEventListener('click', () => {
      order = (order === 'desc') ? 'asc' : 'desc'; // Troca entre asc e desc
      page = 1; // Resetar página
      fetchGames(true); // Limpa jogos antigos e busca de novo
    });
  }
});
