tests/ui/const-generics/issues/issue-60818-struct-constructors.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct Generic<const V: usize>;

fn main() {
    let _ = Generic::<0>;
}


