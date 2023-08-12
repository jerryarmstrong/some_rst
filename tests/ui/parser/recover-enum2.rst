tests/ui/parser/recover-enum2.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    enum Test {
        Var1,
        Var2(String),
        Var3 {
            abc: {}, //~ ERROR: expected type, found `{`
        },
    }

    // recover...
    let a = 1;
    enum Test2 {
        Fine,
    }

    enum Test3 {
        StillFine {
            def: i32,
        },
    }

    {
        // fail again
        enum Test4 {
            Nope(i32 {}) //~ ERROR: found `{`
        }
    }
}


