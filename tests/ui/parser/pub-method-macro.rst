tests/ui/parser/pub-method-macro.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue #18317

mod bleh {
    macro_rules! defn {
        ($n:ident) => (
            fn $n (&self) -> i32 {
                println!("{}", stringify!($n));
                1
            }
        )
    }

    #[derive(Copy, Clone)]
    pub struct S;

    impl S {
        pub defn!(f); //~ ERROR can't qualify macro invocation with `pub`
        //~^ HELP remove the visibility
        //~| HELP try adjusting the macro to put `pub` inside the invocation
    }
}

fn main() {}


