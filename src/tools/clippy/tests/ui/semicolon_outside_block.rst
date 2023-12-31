src/tools/clippy/tests/ui/semicolon_outside_block.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
#![allow(
    unused,
    clippy::unused_unit,
    clippy::unnecessary_operation,
    clippy::no_effect,
    clippy::single_element_loop
)]
#![warn(clippy::semicolon_outside_block)]

macro_rules! m {
    (()) => {
        ()
    };
    (0) => {{
        0
    };};
    (1) => {{
        1;
    }};
    (2) => {{
        2;
    }};
}

fn unit_fn_block() {
    ()
}

#[rustfmt::skip]
fn main() {
    { unit_fn_block() }
    unsafe { unit_fn_block() }

    {
        unit_fn_block()
    }

    { unit_fn_block() };
    unsafe { unit_fn_block() };

    { unit_fn_block(); }
    unsafe { unit_fn_block(); }

    { unit_fn_block(); };
    unsafe { unit_fn_block(); };

    {
        unit_fn_block();
        unit_fn_block()
    };
    {
        unit_fn_block();
        unit_fn_block();
    }
    {
        unit_fn_block();
        unit_fn_block();
    };

    { m!(()) };
    { m!(()); }
    { m!(()); };
    m!(0);
    m!(1);
    m!(2);

    for _ in [()] {
        unit_fn_block();
    }
    for _ in [()] {
        unit_fn_block()
    }

    let _d = || {
        unit_fn_block();
    };
    let _d = || {
        unit_fn_block()
    };

    { unit_fn_block(); };

    unit_fn_block()
}


