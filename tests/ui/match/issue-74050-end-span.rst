tests/ui/match/issue-74050-end-span.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut args = std::env::args_os();
    let _arg = match args.next() {
        Some(arg) => {
            match arg.to_str() {
                //~^ ERROR `arg` does not live long enough
                Some(s) => s,
                None => return,
            }
        }
        None => return,
    };
}


