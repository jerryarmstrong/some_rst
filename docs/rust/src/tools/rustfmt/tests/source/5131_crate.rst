src/tools/rustfmt/tests/source/5131_crate.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-imports_granularity: Crate

use foo::a;
use foo::a;
use foo::b;
use foo::b as b2;
use foo::b::f;
use foo::b::g;
use foo::b::g as g2;
use foo::c;
use foo::d::e;
use qux::h;
use qux::h as h2;
use qux::i;


