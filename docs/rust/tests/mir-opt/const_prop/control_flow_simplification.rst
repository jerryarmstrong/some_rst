tests/mir-opt/const_prop/control_flow_simplification.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: ConstProp
// compile-flags: -Zmir-opt-level=1

trait NeedsDrop: Sized {
    const NEEDS: bool = std::mem::needs_drop::<Self>();
}

impl<This> NeedsDrop for This {}

// EMIT_MIR control_flow_simplification.hello.ConstProp.diff
// EMIT_MIR control_flow_simplification.hello.PreCodegen.before.mir
fn hello<T>(){
    if <bool>::NEEDS {
        panic!()
    }
}

pub fn main() {
    hello::<()>();
    hello::<Vec<()>>();
}


