document.addEventListener('DOMContentLoaded', function() {
    var options = {};
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
});

document.addEventListener('DOMContentLoaded', function() {
    var options = {};
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
});

document.addEventListener('DOMContentLoaded', function() {
    var options = {};
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems, options);
  });