tests/mir-opt/separate_const_switch.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(control_flow_enum)]
#![feature(try_trait_v2)]

use std::ops::ControlFlow;

// EMIT_MIR separate_const_switch.too_complex.SeparateConstSwitch.diff
fn too_complex(x: Result<i32, usize>) -> Option<i32> {
    // The pass should break the outer match into
    // two blocks that only have one parent each.
    // Parents are one of the two branches of the first
    // match, so a later pass can propagate constants.
    match {
        match x {
            Ok(v) => ControlFlow::Continue(v),
            Err(r) => ControlFlow::Break(r),
        }
    } {
        ControlFlow::Continue(v) => Some(v),
        ControlFlow::Break(r) => None,
    }
}

// EMIT_MIR separate_const_switch.identity.SeparateConstSwitch.diff
fn identity(x: Result<i32, i32>) -> Result<i32, i32> {
    Ok(x?)
}

fn main() {
    too_complex(Ok(0));
    identity(Ok(0));
}


