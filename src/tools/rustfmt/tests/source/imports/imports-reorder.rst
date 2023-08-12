src/tools/rustfmt/tests/source/imports/imports-reorder.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true

use path::{C,/*A*/ A, B /* B */, self /* self */};

use {ab, ac, aa, Z, b};


