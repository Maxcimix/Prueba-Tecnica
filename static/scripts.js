document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("rangeForm").addEventListener("submit", function(event) {
        event.preventDefault();
        const start = document.getElementById("start").value;
        const end = document.getElementById("end").value;

        fetch(`/find-perfect-numbers?start=${start}&end=${end}`)
            .then(response => response.json())
            .then(data => {
                const numbers = data.numbers;
                if (numbers.length > 0) {
                    const resultString = "Números Perfectos Encontrados:\n" + numbers.join(", ");
                    alert(resultString);
                } else {
                    alert("No se encontraron números perfectos en el rango especificado.");
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert("Se produjo un error al buscar números perfectos.");
            });
    });
});
