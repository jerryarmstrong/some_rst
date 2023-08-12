tests/ui/feature-gates/feature-gate-min_const_fn.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test use of min_const_fn without feature gate.

const fn foo() -> usize { 0 } // stabilized

trait Foo {
    const fn foo() -> u32; //~ ERROR functions in traits cannot be declared const
    const fn bar() -> u32 { 0 } //~ ERROR functions in traits cannot be declared const
}

impl Foo for u32 {
    const fn foo() -> u32 { 0 } //~ ERROR functions in traits cannot be declared const
}

trait Bar {}

impl dyn Bar {
    const fn baz() -> u32 { 0 } // stabilized
}

static FOO: usize = foo();
const BAR: usize = foo();

macro_rules! constant {
    ($n:ident: $t:ty = $v:expr) => {
        const $n: $t = $v;
    }
}

constant! {
    BAZ: usize = foo()
}

fn main() {
    let x: [usize; foo()] = [];
}


