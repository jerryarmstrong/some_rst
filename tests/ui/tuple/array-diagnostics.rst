tests/ui/tuple/array-diagnostics.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _tmp = [
        ("C200B40A82", 3),
        ("C200B40A83", 4) //~ ERROR: expected function, found `(&'static str, {integer})` [E0618]
        ("C200B40A8537", 5),
    ];
}


