<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
  const ctx = document.getElementById('Chart-Usuarios');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: [{%for usuarios in usuarios.js %}'{{primer.nombre}}',{%endfor%}] ,
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
</script>