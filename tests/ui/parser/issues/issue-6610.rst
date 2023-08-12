tests/ui/parser/issues/issue-6610.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo { fn a() } //~ ERROR expected one of `->`, `;`, `where`, or `{`, found `}`

fn main() {}


