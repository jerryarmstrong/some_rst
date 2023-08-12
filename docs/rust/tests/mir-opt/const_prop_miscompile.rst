tests/mir-opt/const_prop_miscompile.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(raw_ref_op)]

// EMIT_MIR const_prop_miscompile.foo.ConstProp.diff
fn foo() {
    let mut u = (1,);
    *&mut u.0 = 5;
    let y = { u.0 } == 5;
}

// EMIT_MIR const_prop_miscompile.bar.ConstProp.diff
fn bar() {
    let mut v = (1,);
    unsafe {
        *&raw mut v.0 = 5;
    }
    let y = { v.0 } == 5;
}

fn main() {
    foo();
    bar();
}


