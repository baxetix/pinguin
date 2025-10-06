
function selectPenguin(name){
  const el = document.getElementById('penguinChoice');
  el.value = name;
  // smooth highlight
  el.style.background = 'rgba(160,190,240,0.35)';
  setTimeout(()=> el.style.background = '', 900);
  window.scrollTo({top: document.querySelector('.form-section').offsetTop - 20, behavior:'smooth'});
}

document.getElementById('adoptionForm').addEventListener('submit', function(e){
  e.preventDefault();
  const name = document.getElementById('penguinChoice').value || 'your chosen animal';
  alert('Thank you for adopting ' + name + '! We will email you confirmation.');
});
