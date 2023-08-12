tests/ui/imports/resolve_self_super_hint.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    extern crate alloc;
    use alloc::HashMap;
    //~^ ERROR unresolved import `alloc` [E0432]
    //~| HELP a similar path exists
    //~| SUGGESTION self::alloc
    mod b {
        use alloc::HashMap;
        //~^ ERROR unresolved import `alloc` [E0432]
        //~| HELP a similar path exists
        //~| SUGGESTION super::alloc
        mod c {
            use alloc::HashMap;
            //~^ ERROR unresolved import `alloc` [E0432]
            //~| HELP a similar path exists
            //~| SUGGESTION a::alloc
            mod d {
                use alloc::HashMap;
                //~^ ERROR unresolved import `alloc` [E0432]
                //~| HELP a similar path exists
                //~| SUGGESTION a::alloc
            }
        }
    }
}

fn main() {}


