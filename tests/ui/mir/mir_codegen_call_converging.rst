tests/ui/mir/mir_codegen_call_converging.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn converging_fn() -> u64 {
    43
}

fn mir() -> u64 {
    let x;
    loop {
        x = converging_fn();
        break;
    }
    x
}

fn main() {
    assert_eq!(mir(), 43);
}


