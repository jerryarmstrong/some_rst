tests/ui/regions/wf-bound-region-in-object-type.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
#![allow(unused_variables)]
// Test that the `wf` checker properly handles bound regions in object
// types. Compiling this code used to trigger an ICE.

// pretty-expanded FIXME #23616

pub struct Context<'tcx> {
    vec: &'tcx Vec<isize>
}

pub type Cmd<'a> = &'a isize;

pub type DecodeInlinedItem<'a> =
    Box<dyn for<'tcx> FnMut(Cmd, &Context<'tcx>) -> Result<&'tcx isize, ()> + 'a>;

fn foo(d: DecodeInlinedItem) {
}

fn main() { }


