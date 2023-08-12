src/tools/miri/tests/fail/function_calls/exported_symbol_bad_unwind2.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@revisions: extern_block definition both
#![feature(rustc_attrs, c_unwind)]

#[cfg_attr(any(definition, both), rustc_nounwind)]
#[no_mangle]
extern "C-unwind" fn nounwind() {
    //~[definition]^ ERROR: abnormal termination: the program aborted execution
    //~[both]^^ ERROR: abnormal termination: the program aborted execution
    panic!();
}

fn main() {
    extern "C-unwind" {
        #[cfg_attr(any(extern_block, both), rustc_nounwind)]
        fn nounwind();
    }
    unsafe { nounwind() }
    //~[extern_block]^ ERROR: unwinding past a stack frame that does not allow unwinding
}


