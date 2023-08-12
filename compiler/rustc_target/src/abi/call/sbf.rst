compiler/rustc_target/src/abi/call/sbf.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // see https://github.com/llvm/llvm-project/blob/main/llvm/lib/Target/BPF/BPFCallingConv.td
use crate::abi::call::{ArgAbi, FnAbi};

fn classify_ret<Ty>(ret: &mut ArgAbi<'_, Ty>) {
    if ret.layout.is_aggregate() || ret.layout.size.bits() > 64 {
        if ret.layout.size.bits() != 128 {
            ret.make_indirect();
        }
    } else {
        ret.extend_integer_width_to(64);
    }
}

fn classify_arg<Ty>(arg: &mut ArgAbi<'_, Ty>) {
    if arg.layout.is_aggregate() || arg.layout.size.bits() > 64 {
        if arg.layout.size.bits() != 128 {
            arg.make_indirect();
        }
    } else {
        arg.extend_integer_width_to(64);
    }
}

pub fn compute_abi_info<Ty>(fn_abi: &mut FnAbi<'_, Ty>) {
    if !fn_abi.ret.is_ignore() {
        classify_ret(&mut fn_abi.ret);
    }

    for arg in fn_abi.args.iter_mut() {
        if arg.is_ignore() {
            continue;
        }
        classify_arg(arg);
    }
}


