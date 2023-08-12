tests/ui/parser/issues/issue-70388-recover-dotdotdot-rest-pat.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo(i32);

fn main() {
    let Foo(...) = Foo(0); //~ ERROR unexpected `...`
    let [_, ..., _] = [0, 1]; //~ ERROR unexpected `...`
    let _recovery_witness: () = 0; //~ ERROR mismatched types
}


