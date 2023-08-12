tests/ui/parser/bind-struct-early-modifiers.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    struct Foo { x: isize }
    match (Foo { x: 10 }) {
        Foo { ref x: ref x } => {}, //~ ERROR expected `,`
        _ => {}
    }
}


