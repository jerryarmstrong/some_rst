tests/ui/consts/const_in_pattern/no-eq-branch-fail.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(indirect_structural_match)]

struct NoEq;

enum Foo {
    Bar,
    Baz,
    Qux(NoEq),
}

// Even though any of these values can be compared structurally, we still disallow it in a pattern
// because `Foo` does not impl `PartialEq`.
const BAR_BAZ: Foo = if 42 == 42 {
    Foo::Baz
} else {
    Foo::Bar
};

fn main() {
    match Foo::Qux(NoEq) {
        BAR_BAZ => panic!(),
        //~^ ERROR must be annotated with `#[derive(PartialEq, Eq)]`
        _ => {}
    }
}


