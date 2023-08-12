tests/ui/nll/reference-carried-through-struct-field.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Wrap<'a> { w: &'a mut u32 }

fn foo() {
    let mut x = 22;
    let wrapper = Wrap { w: &mut x };
    x += 1; //~ ERROR cannot use `x` because it was mutably borrowed [E0503]
    *wrapper.w += 1;
}

fn main() { }


