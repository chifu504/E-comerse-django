const commentForm = document.getElementById("commentForm");
const commentList = document.querySelector(".comments");

commentForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const commentText = document.getElementById("comment").value;
  const productId = document.getElementById("productId").value;

  fetch("/add-comment/", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': getCookie("csrftoken"),
    },
    body: JSON.stringify({ productId, commentText }),
  })
  .then(function (response) {
    if (response.status === 401) {
      window.location.href = "/cuentas/login/";
    }
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Error al agregar un comentario' + response);
    }
  })
    .then(data => {
      const newComment = document.createElement("div");
      newComment.classList.add("comment");
      newComment.innerHTML = `
        <p>${data.comment}</p>
        <p>Escrito por: ${data.user}</p>
        <p>Fecha: ${data.creacion}</p>
      `;
      commentList.prepend(newComment); //pa poner hasta arriba de la lista de comentarios
      // Limpiar el campo de texto
      document.getElementById("comment").value = ""

    })
    .catch(error => {
      console.error('Error en la solicitud: ' + error);
    });
});
