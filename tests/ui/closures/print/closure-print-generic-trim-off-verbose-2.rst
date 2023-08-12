tests/ui/closures/print/closure-print-generic-trim-off-verbose-2.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Ztrim-diagnostic-paths=off -Zverbose

mod mod1 {
    pub fn f<T: std::fmt::Display>(t: T)
    {
        let x = 20;

        let c = || println!("{} {}", t, x);
        let c1 : () = c;
        //~^ ERROR mismatched types
    }
}

fn main() {
    mod1::f(5i32);
}


