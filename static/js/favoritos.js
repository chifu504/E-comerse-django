const favorite_form = document.getElementById('favorite-form');
const favoriteButton = document.getElementById("favoriteButton");

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

favorite_form.addEventListener('submit',(e)=>{
    e.preventDefault();  
  const product_id = document.getElementById("product_id").value; 
  const data_body = {product_id_body:product_id,}
    fetch("/favorito/",{
      method: 'POST',
      credentials: 'same-origin',
          headers: {
              'Content-Type': 'application/json',
              'X-Requested-With': 'XMLHttpRequest',
              "X-CSRFToken": getCookie("csrftoken"),
          },
          body: JSON.stringify(data_body)
    })
    .then(function (response) {
      if (response.status === 401) {
        // Redirigir al usuario a la página de inicio de sesión
        window.location.href = "/cuentas/login/";
      }
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Error al agregar/quitar el producto a favoritos.' + response);
      }
    })
    .then(function (data) {
      console.log(data.message);
      if (data.is_favorite) {
        favoriteButton.textContent = "Quitar de favoritos";
      } else {
        favoriteButton.textContent = "Agregar a favoritos";
      }
    })
    .catch(function (error) {
      console.error('Error en la solicitud: ' + error);
    });
})