tests/ui/parser/issues/issue-87812-path.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo {
    ( $f:path ) => {{
        let _: usize = $f; //~ERROR
    }};
}

struct Baz;

fn main() {
    foo!(Baz);
}


