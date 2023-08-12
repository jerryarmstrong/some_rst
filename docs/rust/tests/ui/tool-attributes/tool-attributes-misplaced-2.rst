tests/ui/tool-attributes/tool-attributes-misplaced-2.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(rustfmt::skip)] //~ ERROR expected derive macro, found tool attribute `rustfmt::skip`
struct S;

fn main() {
    rustfmt::skip!(); //~ ERROR expected macro, found tool attribute `rustfmt::skip`
}


