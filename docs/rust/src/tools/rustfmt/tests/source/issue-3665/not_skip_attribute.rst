src/tools/rustfmt/tests/source/issue-3665/not_skip_attribute.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![this::is::not::skip::attribute(ouch)]

#[ouch(not,      skip,  me)]
fn main() {}


