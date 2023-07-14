// Obtén todos los botones de eliminar
const removeButtons = document.querySelectorAll('.remove');

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

removeButtons.forEach(button => {
  button.addEventListener('click', (e) => {
    const favoriteId = e.target.dataset.favoriteId; // Obtén el ID del favorito
    
    // Realiza la solicitud fetch para eliminar el favorito
    fetch(`/eliminar-favorito/${favoriteId}/`, {
      method: 'DELETE',
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': getCookie('csrftoken'),
      }
    })
    .then(response => {
      if (response.ok) {
        console.log('Favorito eliminado');
        const wishlistItem = button.closest('.wishlist-item'); //hacemos referencia al boton que se hizo click eliminamos el producto correspondiente
        wishlistItem.remove();
      } else {
        console.error('Error al eliminar el favorito');
      }
    })
    .catch(error => {
      console.error('Error en la solicitud:', error);
    });
  });
});
