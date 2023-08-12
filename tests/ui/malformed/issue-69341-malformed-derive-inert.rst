tests/ui/malformed/issue-69341-malformed-derive-inert.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

struct CLI {
    #[derive(parse())] //~ ERROR expected non-macro attribute, found attribute macro
    path: (),
}


