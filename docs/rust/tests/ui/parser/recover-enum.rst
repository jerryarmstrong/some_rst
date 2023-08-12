tests/ui/parser/recover-enum.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    enum Test {
        Very //~ HELP missing `,`
        Bad(usize) //~ HELP missing `,`
        //~^ ERROR expected one of `(`, `,`, `=`, `{`, or `}`, found `Bad`
        Stuff { a: usize } //~ HELP missing `,`
        //~^ ERROR expected one of `,`, `=`, or `}`, found `Stuff`
        Here
        //~^ ERROR expected one of `,`, `=`, or `}`, found `Here`
    }
}


