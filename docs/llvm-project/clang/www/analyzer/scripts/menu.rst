clang/www/analyzer/scripts/menu.js
==================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: js

    startList = function() {
  if (document.all&&document.getElementById) {
    navRoot = document.getElementById("nav");
    for (i=0; i<navRoot.childNodes.length; i++) {
      node = navRoot.childNodes[i];
      if (node.nodeName=="LI") {
        node.onmouseover=function() {
          this.className+=" over";
        }
        node.onmouseout=function() {
          this.className=this.className.replace(" over", "");
        }
      }
    }
  }
}
window.onload=startList;


