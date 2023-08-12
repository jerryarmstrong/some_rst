tests/ui/did_you_mean/pub-macro-rules.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[macro_use] mod bleh {
    pub macro_rules! foo { //~ ERROR can't qualify macro_rules invocation
        ($n:ident) => (
            fn $n () -> i32 {
                1
            }
        )
    }

}

foo!(meh);

fn main() {
    println!("{}", meh());
}


