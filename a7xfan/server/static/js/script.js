function clear() {
    document.getElementById('drop-albums').classList.toggle('clear');
}
function drop() {
    document.getElementById('drop-albums').classList.toggle('drop');
}
document.getElementById('drop').addEventListener('click', clear);
document.getElementById('drop').addEventListener('click', drop);