src/tools/rustfmt/tests/target/imports/imports-reorder.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true

use path::{self /* self */, /* A */ A, B /* B */, C};

use {aa, ab, ac, b, Z};


