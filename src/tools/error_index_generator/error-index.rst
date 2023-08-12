src/tools/error_index_generator/error-index.js
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    for (const elem of document.querySelectorAll("pre.playground")) {
    if (elem.querySelector(".compile_fail") === null) {
        continue;
    }
    const child = document.createElement("div");
    child.className = "tooltip";
    child.textContent = "ⓘ";
    elem.appendChild(child);
}


