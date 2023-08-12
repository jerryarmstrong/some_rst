tests/ui/borrowck/issue-62107-match-arm-scopes.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let e: i32;
    match e {
        //~^ ERROR E0381
        ref u if true => {}
        ref v if true => {
            let tx = 0;
            &tx;
        }
        _ => (),
    }
}


