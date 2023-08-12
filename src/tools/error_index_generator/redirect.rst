src/tools/error_index_generator/redirect.js
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: js

    (function() {
    if (window.location.hash) {
        let code = window.location.hash.replace(/^#/, '');
        // We have to make sure this pattern matches to avoid inadvertently creating an
        // open redirect.
        if (/^E[0-9]+$/.test(code)) {
            window.location.replace('./error_codes/' + code + '.html');
            return;
        }
    }
    window.location.replace('./error_codes/error-index.html');
})()


