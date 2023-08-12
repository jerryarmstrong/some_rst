src/tools/clippy/tests/ui/result_map_or_into_option.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![warn(clippy::result_map_or_into_option)]

fn main() {
    let opt: Result<u32, &str> = Ok(1);
    let _ = opt.map_or(None, Some);

    let rewrap = |s: u32| -> Option<u32> { Some(s) };

    // A non-Some `f` arg should not emit the lint
    let opt: Result<u32, &str> = Ok(1);
    let _ = opt.map_or(None, rewrap);

    // A non-Some `f` closure where the argument is not used as the
    // return should not emit the lint
    let opt: Result<u32, &str> = Ok(1);
    opt.map_or(None, |_x| Some(1));
}


