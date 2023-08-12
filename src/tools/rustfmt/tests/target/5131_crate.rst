src/tools/rustfmt/tests/target/5131_crate.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-imports_granularity: Crate

use foo::{
    a, b, b as b2,
    b::{f, g, g as g2},
    c,
    d::e,
};
use qux::{h, h as h2, i};


